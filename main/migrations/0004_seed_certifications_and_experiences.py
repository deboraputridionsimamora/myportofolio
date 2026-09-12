from django.db import migrations
from datetime import date


def seed_data(apps, schema_editor):
    Experience = apps.get_model('main', 'Experience')
    Certification = apps.get_model('main', 'Certification')

    Experience.objects.create(
        title="Digital Marketing Intern",
        description="Acted as the primary liaison between mentors and mentees, coordinated Zoom career coaching sessions, and managed tracking systems for attendance and assignments.",
        category="internship",
        ended_at="2026-06-01",
    )
    Experience.objects.create(
        title="Participant, Sekolah BEM Fasilkom (SBF)",
        description="Designed and executed departmental programs, including MUSKAN for talent sourcing and curation, as well as GEKA to appreciate performing contingents across dance, fine arts, music, and drama.",
        category="internship",
        ended_at="2026-05-01",
    )
    Experience.objects.create(
        title="Staff, Sports Department",
        description="Organized sports events and wellness programs for students, managed sports facility logistics, and fostered an active, healthy campus community within Fasilkom UI.",
        category="volunteer",
    )
    Experience.objects.create(
        title="Staff of HR, COMPFEST",
        description="Managed internal relations, supported staff development and engagement initiatives, and helped coordinate administrative processes to ensure smooth operations across divisions.",
        category="volunteer",
    )
    Experience.objects.create(
        title="Mentor, Fundamentals of Programming 0",
        description="Guided incoming students through foundational programming concepts, reviewed their code, and provided constructive feedback to help them build confidence during their early coding journey.",
        category="volunteer",
        ended_at="2026-08-01",
    )
    Experience.objects.create(
        title="Mentor, PSAF Fasilkom UI 2026",
        description="Mentored new students during their faculty orientation, helping them adapt to university life, build peer connections, and navigate the academic environment at Fasilkom UI.",
        category="volunteer",
        ended_at="2025-03-01",
    )
    Experience.objects.create(
        title="Mentor, Open House Fasilkom UI 2025",
        description="Led campus tours and facilitated interactive coding sessions for prospective students, and helped answer their questions about admissions and student life at Fasilkom.",
        category="volunteer",
        ended_at="2025-12-01",
    )
    Experience.objects.create(
        title="Event Division Coordinator, Sospro PMB",
        description="Planned and coordinated the logistics for a social project introducing responsible gadget use to children, from scheduling activities to running the sessions on the day.",
        category="volunteer",
        ended_at="2025-10-01",
    )

    Certification.objects.create(
        title="TOEFL ITP (Institutional Testing Program)",
        issuer="Educational Testing Service (ETS) Global B.V.",
        issue_date=date(2025, 12, 1),
        image="toefl.jpg",
    )
    Certification.objects.create(
        title="Finalist - 9th International Science Olympiad in Mathematics",
        issuer="International Science Olympiad",
        issue_date=date(2025, 1, 1),
        credential_id="NO. 1007/EDUEXPO/ILTI/ISO/2025/01/70215",
        description="Finalist of the 9th International Science Olympiad in Mathematics, selected from more than 24,000 participants.",
        image="iso.jpg",
    )
    Certification.objects.create(
        title="Student Council Executive Committee Appreciation Certificate",
        issuer="SMA Negeri 3 Medan",
        issue_date=date(2024, 4, 1),
        credential_id="20/OSIS/2023/2024",
        image="osis.jpg",
    )
    Certification.objects.create(
        title="Uji Kemahiran Berbahasa Indonesia (UKBI)",
        issuer="Badan Pengembangan dan Pembinaan Bahasa",
        issue_date=date(2025, 7, 1),
        credential_id="SD-BB-0985769",
        description="Achieved an Unggul (Excellent) predicate in the Indonesian Language Proficiency Test (UKBI) held by the Ministry of Education, Culture, Research, and Technology of Indonesia.",
        image="ukbi.jpg",
    )
    Certification.objects.create(
        title="Super Mentor Staff - DDP0 2026",
        issuer="ARUNG 2025",
        issue_date=date(2026, 6, 1),
        description="Recognized as Super Mentor Staff in the DDP0 2026 program organized by ARUNG 2025.",
        image="ddp0.jpg",
    )


def reverse_seed(apps, schema_editor):
    Experience = apps.get_model('main', 'Experience')
    Certification = apps.get_model('main', 'Certification')
    Experience.objects.all().delete()
    Certification.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_certification_image'),  # GANTI sesuai nama file migrasi terakhir yang lo catat di Step 3
    ]

    operations = [
        migrations.RunPython(seed_data, reverse_seed),
    ]