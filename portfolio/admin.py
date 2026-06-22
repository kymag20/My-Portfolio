from django.contrib import admin

from .models import (
    Brand,
    CaseStudy,
    Experience,
    Service,
    SiteProfile,
    SkillChip,
    Stat,
    Testimonial,
    Tool,
    ToolCategory,
    Value,
)


class ToolInline(admin.TabularInline):
    model = Tool
    extra = 1


@admin.register(SiteProfile)
class SiteProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('General', {
            'fields': ('logo_text', 'site_title', 'meta_description'),
        }),
        ('Hero', {
            'fields': (
                'availability_badge',
                'hero_tag',
                'hero_name_line1',
                'hero_name_line2',
                'hero_role',
                'hero_subtitle',
                'hero_initials',
                'profile_photo',
            ),
        }),
        ('Brands Section', {
            'fields': ('brands_label',),
        }),
        ('About Section', {
            'fields': (
                'about_section_tag',
                'about_title',
                'about_bio_1',
                'about_bio_2',
                'about_bio_3',
                'education_icon',
                'education_title',
                'education_subtitle',
            ),
        }),
        ('Services Section', {
            'fields': ('services_section_tag', 'services_title', 'services_subtitle'),
        }),
        ('Experience Section', {
            'fields': ('experience_section_tag', 'experience_title', 'experience_subtitle'),
        }),
        ('Testimonials Section', {
            'fields': ('testimonials_section_tag', 'testimonials_title'),
        }),
        ('Case Studies Section', {
            'fields': ('case_studies_section_tag', 'case_studies_title', 'case_studies_subtitle'),
        }),
        ('Tools Section', {
            'fields': ('tools_section_tag', 'tools_title', 'tools_subtitle'),
        }),
        ('Contact & Footer', {
            'fields': (
                'contact_section_tag',
                'contact_title',
                'contact_subtitle',
                'email',
                'phone',
                'linkedin_url',
                'linkedin_label',
                'toast_message',
                'footer_line1',
                'footer_line2',
            ),
        }),
    )

    def has_add_permission(self, request):
        return not SiteProfile.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ('value', 'label', 'order')
    list_editable = ('order',)


@admin.register(SkillChip)
class SkillChipAdmin(admin.ModelAdmin):
    list_display = ('label', 'order')
    list_editable = ('order',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)


@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'order')
    list_editable = ('order',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'order')
    list_editable = ('order',)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'date_range', 'order')
    list_editable = ('order',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'author_role', 'order')
    list_editable = ('order',)


@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'order')
    list_editable = ('order',)


@admin.register(ToolCategory)
class ToolCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)
    inlines = [ToolInline]
