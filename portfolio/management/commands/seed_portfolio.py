from django.core.management.base import BaseCommand

from portfolio.models import (
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


class Command(BaseCommand):
    help = 'Load default portfolio content into the database'

    def handle(self, *args, **options):
        if SiteProfile.objects.exists() and Stat.objects.exists():
            self.stdout.write(self.style.WARNING('Portfolio data already exists. Skipping seed.'))
            return

        profile = SiteProfile.load()
        profile.about_bio_1 = (
            "Hi, I'm Celito John Regasa — but most people call me CJ. I'm a Virtual Assistant "
            "based in the Philippines with over 7 years of experience helping businesses run smoother, "
            "serve customers better, and grow their presence online."
        )
        profile.about_bio_2 = (
            'My journey started in BPO customer support for global brands like Amazon, eBay, and Choice Hotels, '
            'where I developed a sharp attention to detail and a genuine passion for solving problems. Over time, '
            'I expanded into e-commerce operations, Shopify management, social media, and team training — building '
            'a well-rounded skill set that lets me slot into almost any remote team.'
        )
        profile.about_bio_3 = (
            "I'm a fast learner, self-driven, and thrive in async remote environments. Whether you need someone "
            'to manage your Shopify store, handle customer tickets, or grow your social community — I show up, '
            'I deliver, and I care about your brand as if it were my own.'
        )
        profile.save()

        stats = [
            ('7+', 'Years Experience'),
            ('6', 'Companies'),
            ('13+', 'Tools Mastered'),
            ('3', 'Case Studies'),
        ]
        for order, (value, label) in enumerate(stats):
            Stat.objects.get_or_create(value=value, label=label, defaults={'order': order})

        chips = ['Shopify ✓', 'Zendesk ✓', 'Remote-Ready ✓', 'Philippines 🇵🇭']
        for order, label in enumerate(chips):
            SkillChip.objects.get_or_create(label=label, defaults={'order': order})

        brands = [
            'Amazon', 'eBay', 'Shopify', 'Choice Hotels', 'Svelte Media',
            'TaskUs', 'VXI', 'Sutherland', 'Arya Beauty Co.',
        ]
        for order, name in enumerate(brands):
            Brand.objects.get_or_create(name=name, defaults={'order': order})

        values = [
            ('🎯', 'Detail-Oriented & Reliable', 'I follow SOPs precisely and communicate proactively — no hand-holding needed.'),
            ('🌐', 'Remote-Ready, Always On', 'Based in Philippines (GMT+8), comfortable working with US, AU, and EU time zones.'),
            ('📈', 'Growth-Focused', 'Not just task execution — I think about results, engagement, and how to move the needle.'),
            ('🤝', 'Team Player & Trainer', 'Experienced as an SME and coach — I uplift the whole team, not just myself.'),
        ]
        for order, (icon, title, description) in enumerate(values):
            Value.objects.get_or_create(title=title, defaults={'icon': icon, 'description': description, 'order': order})

        services = [
            ('💬', 'Customer Support', 'Full-channel support via live chat, email, and phone. Experienced with Zendesk, Help Scout, and RingCentral to deliver fast, brand-consistent responses.'),
            ('🛍️', 'Shopify Management', 'End-to-end Shopify store setup, product uploads, customization, and ongoing maintenance. Skilled in supporting merchants and resolving store issues.'),
            ('📱', 'Social Media Management', 'Content scheduling, community engagement, comment & DM management across Facebook, Instagram, and YouTube — all aligned to brand guidelines and SOPs.'),
            ('📣', 'Facebook & Instagram Ads', 'Creation and management of paid social campaigns. Hands-on experience running ads for e-commerce brands through Facebook Business Suite.'),
            ('👥', 'Community Management', 'Growing and engaging online communities through organic outreach, follower engagement, and consistent interaction — with performance reports included.'),
            ('📋', 'Training & Coaching', 'SME experience preparing training materials, evaluating team performance, and coaching agents on escalations and complex support cases.'),
        ]
        for order, (icon, title, description) in enumerate(services):
            Service.objects.get_or_create(title=title, defaults={'icon': icon, 'description': description, 'order': order})

        experiences = [
            (
                'Sep 2023 — May 2026',
                'SME / Trainer & Social Media Support',
                'Svelte Media Inc.',
                [
                    'Supported teammates with escalated concerns and complex cases',
                    'Prepared training materials and evaluated team performance',
                    'Provided coaching and knowledge support across the team',
                    'Managed Facebook, Instagram, and YouTube comments following brand guidelines',
                ],
            ),
            (
                'Feb 2023 — Sep 2023',
                'Shopify Support Advisor',
                'TaskUs Clark',
                [
                    'Supported Shopify merchants through chat and email channels',
                    'Assisted with store setup, customization, product listings, and troubleshooting',
                ],
            ),
            (
                'Freelance',
                'E-commerce & Social Media Virtual Assistant',
                'Arya Beauty Co.',
                [
                    'Created and managed full Shopify store including setup and product uploads',
                    'Created and ran Facebook and Instagram ad campaigns',
                    'Scheduled social media content using Hootsuite',
                    'Provided customer support via Zendesk, Help Scout, and RingCentral',
                    'Grew community through engagement, follower invitations, and daily/weekly reports',
                ],
            ),
            (
                'May 2021 — Jan 2023',
                'Customer Support Representative — eBay',
                'VXI Clark',
                [
                    'Provided chat and email support for buyers and sellers on the eBay platform',
                    'Assisted with orders, refunds, delivery concerns, and seller listings',
                ],
            ),
            (
                'Mar 2020 — Mar 2021',
                'Inbound Sales Representative — Choice Hotels',
                'Sitel Tarlac',
                [
                    'Assisted customers with hotel reservations, availability, and services across USA & Canada',
                ],
            ),
            (
                'May 2018 — Sep 2019',
                'Customer Support Representative — Amazon & Credit One Bank',
                'Sutherland',
                [
                    'Assisted customers with account inquiries, payments, orders, deliveries, and claims',
                ],
            ),
        ]
        for order, (date_range, title, company, bullets) in enumerate(experiences):
            Experience.objects.get_or_create(
                title=title,
                company=company,
                defaults={
                    'date_range': date_range,
                    'bullets': '\n'.join(bullets),
                    'order': order,
                },
            )

        testimonials = [
            (
                "CJ is one of the most reliable VAs I've worked with. He handles our Shopify store and customer support with zero supervision — always on time, always thorough.",
                'Carol',
                'E-commerce Store Owner · Arya Beauty Co.',
                'C',
            ),
            (
                'His training materials were clear, actionable, and helped onboard our new agents 40% faster. CJ truly understands what a support team needs to succeed.',
                'Team Manager',
                'Operations · Svelte Media Inc.',
                'S',
            ),
        ]
        for order, (quote, name, role, initial) in enumerate(testimonials):
            Testimonial.objects.get_or_create(
                author_name=name,
                defaults={
                    'quote': quote,
                    'author_role': role,
                    'author_initial': initial,
                    'order': order,
                },
            )

        case_studies = [
            (
                '01',
                'Customer Support Excellence',
                'Provided customer support for high-volume accounts, assisting customers with inquiries, troubleshooting concerns, account issues, and service-related questions while maintaining a professional and customer-first approach.',
                [
                    'Customers expected fast and accurate resolutions, often with urgent concerns',
                    'Handling a large number of interactions required strong communication and problem-solving',
                    'Maintaining high satisfaction across all channels simultaneously',
                ],
                [
                    'Responded to customer inquiries via phone, email, and chat',
                    'Investigated and resolved customer concerns efficiently',
                    'Documented interactions accurately in CRM systems',
                    'Escalated complex cases when necessary',
                    'Maintained professionalism during high-volume periods',
                ],
                [
                    'Consistently delivered positive customer experiences',
                    'Improved customer satisfaction through timely issue resolution',
                    'Maintained accuracy while managing multiple cases',
                    'Contributed to smooth day-to-day support operations',
                ],
            ),
            (
                '02',
                'Shopify & E-commerce Virtual Assistance',
                'Supported e-commerce operations by managing Shopify store tasks, processing orders, updating products, and assisting customers throughout their purchasing journey.',
                [
                    'E-commerce businesses require accurate product info and organized order management',
                    'Responsive customer support needed to ensure smooth operations',
                    'Maintaining up-to-date store information across a growing catalog',
                ],
                [
                    'Managed Shopify product listings and updates',
                    'Processed customer orders and monitored fulfillment',
                    'Assisted customers with order tracking and product inquiries',
                    'Coordinated with suppliers and team members when needed',
                    'Maintained accurate store information and inventory updates',
                ],
                [
                    'Helped maintain efficient store operations',
                    'Reduced product listing and order processing errors',
                    'Supported a positive customer shopping experience',
                    'Ensured accurate and up-to-date store information',
                ],
            ),
            (
                '03',
                'Social Media & Community Management',
                'Managed social media activities and online community engagement to help businesses maintain a professional and active online presence.',
                [
                    'Businesses need consistent content and audience engagement',
                    'Strengthening brand awareness and building audience trust requires constant effort',
                    'Maintaining brand voice consistently across multiple platforms',
                ],
                [
                    'Scheduled and published social media content',
                    'Responded to comments, messages, and inquiries',
                    'Assisted with content planning and organization',
                    'Monitored audience engagement and interactions',
                    'Helped maintain brand consistency across platforms',
                ],
                [
                    'Improved consistency of social media activity',
                    'Increased audience interaction and engagement',
                    'Strengthened online brand presence',
                    'Supported overall marketing and communication efforts',
                ],
            ),
        ]
        for order, (number, title, summary, challenges, actions, outcomes) in enumerate(case_studies):
            CaseStudy.objects.get_or_create(
                title=title,
                defaults={
                    'number': number,
                    'summary': summary,
                    'challenges': '\n'.join(challenges),
                    'actions': '\n'.join(actions),
                    'outcomes': '\n'.join(outcomes),
                    'order': order,
                },
            )

        tool_data = {
            'CRM & Support': ['Zendesk', 'Help Scout', 'RingCentral', 'CRM'],
            'E-commerce': ['Shopify'],
            'Social Media': ['Hootsuite', 'Facebook Business Suite', 'InviteLikeComment', 'Instagram'],
            'Design': ['Canva'],
            'Productivity': ['Google Workspace', 'Microsoft Office', 'Slack', 'Discord', 'Notion'],
        }
        for cat_order, (category_name, tools) in enumerate(tool_data.items()):
            category, _ = ToolCategory.objects.get_or_create(
                name=category_name,
                defaults={'order': cat_order},
            )
            for tool_order, tool_name in enumerate(tools):
                Tool.objects.get_or_create(
                    category=category,
                    name=tool_name,
                    defaults={'order': tool_order},
                )

        self.stdout.write(self.style.SUCCESS('Portfolio content loaded successfully.'))
