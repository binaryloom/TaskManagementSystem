from rest_framework.generics import CreateAPIView


class CreateAPIView(CreateAPIView):
    pass


from abc import ABC, abstractmethod
from typing import Any, Dict

from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalDeleteView,
    BSModalReadView,
    BSModalUpdateView,
)
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db import models
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import DetailView, FormView, ListView, TemplateView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django_filters.views import FilterView
from extra_views import SearchableListMixin
from versity_info.enums import Status

from abstract.utils import duplicate_objects


class BaseView(View):
    pass


class BaseTemplateView(TemplateView):
    pass


class BaseFormView(FormView):
    pass


class BaseListView(ListView):
    paginate_by = 12
    template_name = "list.html"


class BaseDetailView(DetailView):
    template_name = "shared/template/detail_raw.html"


class BaseCreateView(CreateView):
    template_name = "form.html"


class BaseFilterView(FilterView):
    paginate_by = 12
    template_name = "shared/template/list_raw.html"


class BaseDetailFilteredView(BaseListView):
    paginate_by = 12
    # SHOUROV: please implement the get_queryset implementation Required.
    template_name = "shared/template/detail_express_raw.html"

    def get_parent(self):
        return self.parent_model._default_manager.get(pk=self.kwargs.get("pk"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs.get("pk") is not None:
            context["object"] = self.get_parent()

        return context


class BaseDetailFilteredFilterView(FilterView):
    # SHOUROV: please implement the pagination for search data.
    paginate_by = 12
    # SHOUROV: please implement the get_queryset implementation Required.
    template_name = "shared/template/detail_express_raw.html"

    def get_parent(self):
        return self.parent_model._default_manager.get(pk=self.kwargs.get("pk"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs.get("pk") is not None:
            context["object"] = self.get_parent()
        context["page_range"] = context["paginator"].get_elided_page_range(
            number=context["page_obj"].number, on_each_side=1, on_ends=2
        )
        return context


class BaseCreateView(CreateView):
    # SHOUROV: need more polishing
    object = None  # POSSIBLE FIX : AttributeError: 'CreateView' object has no attribute 'object'
    template_name = "form.html"
    related_form_classes = []
    related_fields = []
    related_models = []
    reverse_relations = []
    reverse_related_fields = []

    def __init__(self, **kwargs):
        if self.related_form_classes:
            if not self.related_fields and not self.reverse_related_fields:
                for index, related_form_class in enumerate(self.related_form_classes):
                    related_model = related_form_class._meta.model
                    if self.reverse_relations[index]:
                        for field in related_model._meta.get_fields():
                            if field.is_relation and field.related_model == self.model:
                                self.related_fields.append(field.name)
                        for field in self.model._meta.get_fields():
                            if (
                                field.is_relation
                                and field.related_model == related_model
                            ):
                                self.reverse_related_fields.append(field.name)
                    else:
                        for field in self.model._meta.get_fields():
                            if (
                                field.is_relation
                                and field.related_model == related_model
                            ):
                                self.related_fields.append(field.name)
                        for field in related_model._meta.get_fields():
                            if field.is_relation and field.related_model == self.model:
                                self.reverse_related_fields.append(field.name)
                    self.related_models.append(related_model)
        super().__init__(**kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.related_form_classes:
            context["related_forms"] = self.related_form_classes
        if kwargs.get("related_forms") and self.related_fields:
            context["related_forms"] = kwargs.get("related_forms")
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        print("RAW DATA POST : ", request.POST)
        print("RAW DATA FILE: ", request.FILES)
        if not self.related_fields:
            print("single form section")
            if form.is_valid():
                print("valid form")
                return self.form_valid(form)
            else:
                print("invalid form")
                print(form)
                return self.form_invalid(form)

        related_forms = []
        # form = self.form_class(request.POST, request.FILES)
        for related_form_class in self.related_form_classes:
            related_form = related_form_class(request.POST, request.FILES)
            related_forms.append(related_form)
        print("BaseCreateView related_forms section")
        if form.is_valid() and all(
            [related_form.is_valid() for related_form in related_forms]
        ):
            return self.form_valid(form, related_forms=related_forms)
        return self.form_invalid(form, related_forms=related_forms)

    def form_valid(self, form, **kwargs):
        if not kwargs.get("related_forms") and not self.related_fields:
            print("super form valid")
            for key, value in form.cleaned_data.items():
                print(f"{key}: {value}")
            return super().form_valid(form)
        if form.is_valid() and all(
            [related_form.is_valid() for related_form in kwargs.get("related_forms")]
        ):
            self.object = form.save()
            for index, related_form in enumerate(kwargs.get("related_forms")):
                if self.reverse_relations[index]:
                    related_object = duplicate_objects(
                        self.related_models[index](**related_form.cleaned_data),
                        getattr(
                            self.object, self.reverse_related_fields[index]
                        ).first(),
                        skip_field=self.related_fields[index],
                    )
                    related_object.save()
                else:
                    related_object = related_form.save()
                    setattr(self.object, self.related_fields[index], related_object)
                    self.object.save()
            return redirect(self.get_success_url())

    def form_invalid(self, form, **kwargs):
        print("Invalid FORM field From BaseCreateView")
        print("*****************************************************************")
        for field, errors in form.errors.items():
            print(f"{field}: {', '.join(errors)}")
            messages.error(self.request, f"{field}: {', '.join(errors)}")
        if not kwargs.get("related_forms") and not self.related_fields:
            return super().form_invalid(form)
        related_forms = kwargs.get("related_forms")
        for related_form in related_forms:
            for field, errors in related_form.errors.items():
                print(f"{field}: {', '.join(errors)}")
                messages.error(
                    self.request, f"Related Form {field}: {', '.join(errors)}"
                )
        return super().render_to_response(
            self.get_context_data(form=form, related_forms=kwargs.get("related_form"))
        )

    #     print('Invalid FORM field')
    #     print('*****************************************************************')

    #     print("Form errors:", form.errors)
    #     print("Non-field errors:", form.non_field_errors)

    #     print()
    #     print()
    #     print()
    #     print()
    #     print()

    #     for field, errors in form.errors.items():
    #         print(f"{field}: {', '.join(errors)}")
    #         messages.error(self.request, f"{field}: {', '.join(errors)}")
    #     # for key, value in form.cleaned_data.items():
    #     #     print(f"{key}: {value}")

    #     print()
    #     print()
    #     print()
    #     print()
    #     print()

    #     if not kwargs.get("related_forms") and not self.related_fields:
    #         return super().form_invalid(form)
    #     return super().render_to_response(
    #         self.get_context_data(form=form, related_forms=kwargs.get("related_forms"))
    #     )


class BaseCreateFormsetView(BaseCreateView):
    # HRIDOY: Blank form is also submitted
    formsets = []
    formset_fields = []
    formset_models = []
    reverse_formset_fields = []
    formset_classes = []
    formset_queries = []
    formset_reverse_relations = []

    def __init__(self, **kwargs):
        if self.formset_classes:
            if (
                not self.formsets
                and not self.formset_fields
                and not self.reverse_formset_fields
            ):
                for index, formset_class in enumerate(self.formset_classes):
                    self.formsets.append(
                        formset_class(
                            queryset=self.formset_queries[index], prefix=f"{index}"
                        )
                    )
                    self.formset_models.append(self.formsets[index][0]._meta.model)
                    if self.formset_reverse_relations[index]:
                        pass
                    else:
                        for field in self.model._meta.get_fields():
                            if (
                                isinstance(field, models.ManyToManyField)
                                and field.related_model is self.formset_models[index]
                            ):
                                self.formset_fields.append(field.name)

        super().__init__(**kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formsets"] = self.formsets or None
        return context

    def post(self, request, *args, **kwargs):
        if not self.formset_classes:
            return super().post(request, *args, **kwargs)
        related_formsets = []
        form = self.form_class(request.POST, request.FILES)
        for index, formset_class in enumerate(self.formset_classes):
            related_formset = formset_class(
                request.POST, request.FILES, prefix=f"{index}"
            )
            related_formsets.append(related_formset)
        if form.is_valid() and all(
            [related_formset.is_valid() for related_formset in related_formsets]
        ):
            return self.form_valid(form, related_formsets=related_formsets)
        return self.form_invalid(form, related_formsets=related_formsets)

    def form_valid(self, form, **kwargs):
        if not kwargs.get("related_formsets"):
            return super().form_valid(form)
        print("form.is_valid()", form.is_valid())
        print(
            "all( related forms) ",
            all(
                [
                    related_formset.is_valid()
                    for related_formset in kwargs.get("related_formsets")
                ]
            ),
        )
        if form.is_valid() and all(
            [
                related_formset.is_valid()
                for related_formset in kwargs.get("related_formsets")
            ]
        ):
            self.object = form.save(commit=True)
            for index, related_formset in enumerate(kwargs.get("related_formsets")):
                print("working with ", self.formset_fields[index])
                tmp_objects = []
                for form in related_formset:
                    if form.is_valid():
                        tmp_object = form.save(commit=True)
                        tmp_objects.append(tmp_object)
                if tmp_objects:
                    tmp_fields = getattr(self.object, self.formset_fields[index])
                    tmp_objects += getattr(
                        self.object, self.formset_fields[index]
                    ).all()
                    tmp_fields.set(tmp_objects)
                    self.object.save()
        return redirect(self.get_success_url())

    def form_invalid(self, form, **kwargs):
        for field, errors in form.errors.items():
            print(f"{field}: {', '.join(errors)}")
            messages.error(self.request, f"{field}: {', '.join(errors)}")
        return super().form_invalid(form)


class BaseCreateListView(BaseCreateView, BaseListView):
    template_name = "list_form.html"

    # SHOUROV: invalid form submission is not done
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class BaseRelatedCreateView(CreateView):
    object = None
    related_form_class = None
    related_field = None
    related_model = None
    template_name = "form.html"

    def __init__(self, **kwargs: Any) -> None:
        if self.related_form_class is not None:
            self.related_model = self.related_form_class._meta.model
            for field in self.model._meta.get_fields():
                if field.is_relation and field.related_model == self.related_model:
                    self.related_field = field.name
        super().__init__(**kwargs)

    def get_success_message(self, cleaned_data):
        # not working
        return "New object was created successfully"

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return self.object.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.related_form_class is not None:
            # SHOUROV: THIS THING MAY BRIC
            context["related_form"] = self.related_form_class
        if related_form := context.get("related_form"):
            context["related_form"] = related_form
        return context

    def post(self, request, *args, **kwargs):
        print("request POST : ", request.POST)
        print("request FILES : ", request.FILES)
        form = self.form_class(request.POST, request.FILES)
        related_form = self.related_form_class(request.POST, request.FILES)
        if form.is_valid() and related_form.is_valid():
            return self.form_valid(form, related_form)
        return self.form_invalid(form, related_form=related_form)

    def form_valid(self, form, related_form):
        self.object = form.save()
        self.related_object = related_form.save()
        if self.related_field is not None:
            setattr(self.object, self.related_field, self.related_object)
            self.object.save()
        return redirect(self.get_success_url())

    def form_invalid(self, form, *args, **kwargs):
        print("Invalid FORM field From BaseRelatedCreateView")
        print("*****************************************************************")
        for field, errors in form.errors.items():
            print(f"{field}: {', '.join(errors)}")
            messages.error(self.request, f"{field}: {', '.join(errors)}")
        if not kwargs.get("related_form") and not self.related_field:
            return super().form_invalid(form)
        related_form = kwargs.get("related_form")
        for field, errors in related_form.errors.items():
            print(f"{field}: {', '.join(errors)}")
            messages.error(self.request, f"Related Form {field}: {', '.join(errors)}")
        return super().render_to_response(
            self.get_context_data(form=form, related_form=kwargs.get("related_form"))
        )


class BaseSearchView(SearchableListMixin, BaseListView):
    def get_queryset(self):
        # TODO: implement all the pairs
        tmp_query = self.get_search_query()
        # for pair in self.get_search_fields_with_filters():
        #     pass
        return (
            self.document.search()  # type:ignore
            .filter(
                "multi_match",
                query=tmp_query,
                fields=["name", "name_utf"],
                fuzziness="auto",
            )
            .to_queryset()
        )


class BaseUpdateView(UpdateView):
    template_name = "base_form.html"

    def form_invalid(self, form):
        """
        If the form is invalid, re-render the context data with the data-filled
        form and the error messages.
        """
        print(form.errors)
        print("RAW DATA POST : ", self.request.POST)
        print("RAW DATA FILE: ", self.request.FILES)
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return self.object.get_absolute_url()  # type: ignore


class BaseDeleteView(DeleteView):
    template_name = "delete.html"


class BaseBSCreateView(BSModalCreateView):
    pass


class BaseBSReadView(BSModalReadView):
    pass


class BaseBSUpdateView(BSModalUpdateView):
    pass


class BaseBSDeleteView(BSModalDeleteView):
    template_name = "shared/form/modal_delete.html"
    success_message = "object Deleted"
