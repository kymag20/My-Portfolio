from django.db import models


class SiteProfile(models.Model):
    logo_text = models.CharField(max_length=50, default='CJR')
    site_title = models.CharField(max_length=200, default='CJ Regasa — Virtual Assistant Portfolio')
    meta_description = models.TextField(
        default='Virtual Assistant, Customer Support Specialist, Shopify & E-commerce VA based in the Philippines.'
    )

    availability_badge = models.CharField(
        max_length=300,
        default='Available for Full-Time VA, Customer Support, Shopify & E-commerce Roles',
    )
    hero_tag = models.CharField(max_length=200, default='Philippines · Remote · GMT+8')
    hero_name_line1 = models.CharField(max_length=100, default='Celito John')
    hero_name_line2 = models.CharField(max_length=100, default='Regasa.')
    hero_role = models.CharField(
        max_length=300,
        default='Virtual Assistant | Customer Support Specialist | Shopify & E-commerce VA',
    )
    hero_subtitle = models.TextField(
        default=(
            'Helping businesses streamline operations, deliver excellent customer service, '
            'and grow their online presence through reliable virtual assistance, e-commerce support, '
            'and social media management.'
        )
    )
    hero_initials = models.CharField(max_length=10, default='CJ')
    profile_photo = models.FileField(upload_to='profile/', blank=True, null=True)

    brands_label = models.CharField(max_length=200, default="Brands & Companies I've Worked With")

    about_section_tag = models.CharField(max_length=100, default='About Me')
    about_title = models.CharField(max_length=200, default='Your Reliable Remote Partner.')
    about_bio_1 = models.TextField(blank=True)
    about_bio_2 = models.TextField(blank=True)
    about_bio_3 = models.TextField(blank=True)
    education_icon = models.CharField(max_length=10, default='🎓')
    education_title = models.CharField(max_length=200, default='BSEd English · Batch 2020')
    education_subtitle = models.CharField(max_length=200, default='Tarlac State University')

    services_section_tag = models.CharField(max_length=100, default='What I Do')
    services_title = models.CharField(max_length=200, default='Services Offered.')
    services_subtitle = models.TextField(
        default='From customer support to e-commerce and social media — I help businesses run smoother and grow online.'
    )

    experience_section_tag = models.CharField(max_length=100, default='Career Timeline')
    experience_title = models.CharField(max_length=200, default='Professional Experience.')
    experience_subtitle = models.TextField(
        default='7+ years across BPO, e-commerce, social media, and team training.'
    )

    testimonials_section_tag = models.CharField(max_length=100, default='Kind Words')
    testimonials_title = models.CharField(max_length=200, default='What Clients Say.')

    case_studies_section_tag = models.CharField(max_length=100, default='Real Work, Real Results')
    case_studies_title = models.CharField(max_length=200, default='Case Studies.')
    case_studies_subtitle = models.TextField(
        default='Detailed breakdowns of challenges, actions, and outcomes from real projects.'
    )

    tools_section_tag = models.CharField(max_length=100, default='Tech Stack')
    tools_title = models.CharField(max_length=200, default='Tools & Platforms.')
    tools_subtitle = models.TextField(
        default='The platforms and software I use daily to deliver results.'
    )

    contact_section_tag = models.CharField(max_length=100, default='Get In Touch')
    contact_title = models.CharField(max_length=200, default='Ready to Work Together?')
    contact_subtitle = models.TextField(
        default=(
            "Send me a message and I'll get back to you within 24 hours. "
            "I'm open to full-time, part-time, and project-based remote roles."
        )
    )
    email = models.EmailField(default='celitojohn@gmail.com')
    phone = models.CharField(max_length=50, default='+63 981 717 4999')
    linkedin_url = models.URLField(blank=True, default='https://www.linkedin.com/in/cj-regasa')
    linkedin_label = models.CharField(max_length=100, default='LinkedIn — CJ Regasa')
    toast_message = models.CharField(
        max_length=200,
        default="Message sent! I'll get back to you within 24 hours.",
    )

    footer_line1 = models.CharField(
        max_length=300,
        default="© 2026 Celito John Regasa · O'Donnell, Capas, Tarlac, Philippines",
    )
    footer_line2 = models.CharField(
        max_length=200,
        default='Available for new projects · Philippines (GMT+8)',
    )

    class Meta:
        verbose_name = 'Site Profile'
        verbose_name_plural = 'Site Profile'

    def __str__(self):
        return self.site_title

    @classmethod
    def load(cls):
        profile, _ = cls.objects.get_or_create(pk=1)
        return profile

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class Stat(models.Model):
    value = models.CharField(max_length=20, help_text='Example: 7+')
    label = models.CharField(max_length=100, help_text='Example: Years Experience')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Stat'
        verbose_name_plural = 'Stats'

    def __str__(self):
        return f'{self.value} — {self.label}'


class SkillChip(models.Model):
    label = models.CharField(max_length=100, help_text='Example: Shopify ✓')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Skill Chip'
        verbose_name_plural = 'Skill Chips'

    def __str__(self):
        return self.label


class Brand(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name


class Value(models.Model):
    icon = models.CharField(max_length=10, default='🎯')
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Value'
        verbose_name_plural = 'Values'

    def __str__(self):
        return self.title


class Service(models.Model):
    icon = models.CharField(max_length=10, default='💬')
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title


class Experience(models.Model):
    date_range = models.CharField(max_length=100, help_text='Example: Sep 2023 — May 2026')
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    bullets = models.TextField(
        help_text='One bullet point per line.',
        blank=True,
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Experience'
        verbose_name_plural = 'Experience'

    def __str__(self):
        return f'{self.title} @ {self.company}'

    def bullet_list(self):
        return [line.strip() for line in self.bullets.splitlines() if line.strip()]


class Testimonial(models.Model):
    quote = models.TextField()
    author_name = models.CharField(max_length=100)
    author_role = models.CharField(max_length=200)
    author_initial = models.CharField(max_length=5, help_text='Single letter for avatar')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return self.author_name


class CaseStudy(models.Model):
    number = models.CharField(max_length=5, help_text='Example: 01')
    title = models.CharField(max_length=200)
    summary = models.TextField()
    challenges = models.TextField(help_text='One item per line.')
    actions = models.TextField(help_text='One item per line.')
    outcomes = models.TextField(help_text='One item per line.')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Case Study'
        verbose_name_plural = 'Case Studies'

    def __str__(self):
        return self.title

    def challenge_list(self):
        return [line.strip() for line in self.challenges.splitlines() if line.strip()]

    def action_list(self):
        return [line.strip() for line in self.actions.splitlines() if line.strip()]

    def outcome_list(self):
        return [line.strip() for line in self.outcomes.splitlines() if line.strip()]


class ToolCategory(models.Model):
    name = models.CharField(max_length=100, help_text='Example: CRM & Support')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Tool Category'
        verbose_name_plural = 'Tool Categories'

    def __str__(self):
        return self.name


class Tool(models.Model):
    category = models.ForeignKey(ToolCategory, related_name='tools', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Tool'
        verbose_name_plural = 'Tools'

    def __str__(self):
        return self.name
