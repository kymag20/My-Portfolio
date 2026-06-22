from django.shortcuts import render

from .models import (
    Brand,
    CaseStudy,
    Experience,
    Service,
    SiteProfile,
    SkillChip,
    Stat,
    Testimonial,
    ToolCategory,
    Value,
)


def home(request):
    profile = SiteProfile.load()
    context = {
        'profile': profile,
        'stats': Stat.objects.all(),
        'skill_chips': SkillChip.objects.all(),
        'brands': Brand.objects.all(),
        'values': Value.objects.all(),
        'services': Service.objects.all(),
        'experiences': Experience.objects.all(),
        'testimonials': Testimonial.objects.all(),
        'case_studies': CaseStudy.objects.all(),
        'tool_categories': ToolCategory.objects.prefetch_related('tools'),
    }
    return render(request, 'portfolio/index.html', context)
