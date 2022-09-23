# Generated by Django 4.1.1 on 2022-09-23 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='job_title',
            field=models.CharField(choices=[('MARKETING SPECIALIST', 'Marketing Specialist'), ('MARKETING MANAGER', 'Marketing manager'), ('MARKETING DIRECTOR', 'Marketing Director'), ('GRAPHIC DESIGNER', 'Graphic Designer'), ('MARKETING RESEARCH ANALYST', 'Marketing Research Analyst'), ('MARKETING COMMUNICATIONS MANAGER', 'Marketing Communications Manager'), ('MARKETING CONSULTAN', 'Marketing Consultant'), ('PRODUCT MANAGER', 'Product Manager'), ('PUBLIC RELATIONS', 'Public Relations'), ('SOCIAL MEDIA ASSISTANT', 'Social Media Assistant'), ('BRAND MANAGER', 'Brand Manager'), ('SEO MANAGER', 'Seo Manager'), ('CONTENT MARKETING MANAGER', 'Content Marketing Manager'), ('MEDIA BUYER', 'Media Buyer'), ('DIGITAL MARKETING MANAGER', 'Digital Marketing Manager'), ('ECOMMERCE MARKETING SPECIALIST', 'Ecommerce Marketing Specialist'), ('BRAND STRATEGIST', 'Brand Strategist'), ('MEDIA RELATIONS COORDINATOR', 'Media Relations Coordinator'), ('IT PROFESSIONAL', 'IT Professional'), ('UX DESIGNER & UI DEVELOPER', 'UI Designer & UI Developer'), ('SQL DEVELOPER', 'SQL Developer'), ('WEB DESIGNER', 'Web Designer'), ('WEB DEVELOPER', 'Web Developer'), ('HELP DESK WORKER/DESKTOP SUPPORT', 'Help Desk Worker/desktop Support'), ('SOFTWARE ENGINEER', 'Software Engineer'), ('DATA ENTRY', 'Data Entry'), ('COMPUTER PROGRAMMER', 'Computer Programmer'), ('NETWORK ADMINISTRATOR', 'Network Administrator'), ('ARTIFICIAL INTELLIGENCE ENGINEER', 'Artificial Intelligence Engineer'), ('IT MANAGER', 'IT Manager'), ('TECHNICAL SPECIALIST', 'Technical Specialist'), ('APPLICATION DEVELOPER', 'Application Developer'), ('BACKEND DEVELOPER', 'Backend Developer'), ('FRONTEND DEVELOPER', 'Frontend Developer'), ('ADMINISTRATIVE ASSISTANT', 'Administrative Assistant'), ('RECEPTIONIST', 'Receptionist'), ('OFFICE MANAGER', 'Office Manager'), ('AUDITING CLERK', 'Auditing Clerk'), ('BOOKKEEPER', 'Bookkeeper'), ('ACCOUNT EXECUTIVE', 'Account Executive'), ('BRANCH MANAGER', 'Branch Manager'), ('BUSINESS MANAGER', 'Business Manager'), ('QUALITY CONTROL COORDINATOR', 'Quality Control Coordinator'), ('ADMINISTRATIVE MANAGER', 'Administrative Manager'), ('HUMAN RESOURCES', 'Human Resources'), ('OFFICE ASSISTANT', 'Office Assistant'), ('SECRETARY', 'Secretary'), ('ACCOUNT COLLECTOR', 'Account Collector')], max_length=100),
        ),
        migrations.AlterField(
            model_name='job',
            name='position',
            field=models.CharField(blank=True, choices=[('MARKETING SPECIALIST', 'Marketing Specialist'), ('MARKETING MANAGER', 'Marketing manager'), ('MARKETING DIRECTOR', 'Marketing Director'), ('GRAPHIC DESIGNER', 'Graphic Designer'), ('MARKETING RESEARCH ANALYST', 'Marketing Research Analyst'), ('MARKETING COMMUNICATIONS MANAGER', 'Marketing Communications Manager'), ('MARKETING CONSULTAN', 'Marketing Consultant'), ('PRODUCT MANAGER', 'Product Manager'), ('PUBLIC RELATIONS', 'Public Relations'), ('SOCIAL MEDIA ASSISTANT', 'Social Media Assistant'), ('BRAND MANAGER', 'Brand Manager'), ('SEO MANAGER', 'Seo Manager'), ('CONTENT MARKETING MANAGER', 'Content Marketing Manager'), ('MEDIA BUYER', 'Media Buyer'), ('DIGITAL MARKETING MANAGER', 'Digital Marketing Manager'), ('ECOMMERCE MARKETING SPECIALIST', 'Ecommerce Marketing Specialist'), ('BRAND STRATEGIST', 'Brand Strategist'), ('MEDIA RELATIONS COORDINATOR', 'Media Relations Coordinator'), ('IT PROFESSIONAL', 'IT Professional'), ('UX DESIGNER & UI DEVELOPER', 'UI Designer & UI Developer'), ('SQL DEVELOPER', 'SQL Developer'), ('WEB DESIGNER', 'Web Designer'), ('WEB DEVELOPER', 'Web Developer'), ('HELP DESK WORKER/DESKTOP SUPPORT', 'Help Desk Worker/desktop Support'), ('SOFTWARE ENGINEER', 'Software Engineer'), ('DATA ENTRY', 'Data Entry'), ('COMPUTER PROGRAMMER', 'Computer Programmer'), ('NETWORK ADMINISTRATOR', 'Network Administrator'), ('ARTIFICIAL INTELLIGENCE ENGINEER', 'Artificial Intelligence Engineer'), ('IT MANAGER', 'IT Manager'), ('TECHNICAL SPECIALIST', 'Technical Specialist'), ('APPLICATION DEVELOPER', 'Application Developer'), ('BACKEND DEVELOPER', 'Backend Developer'), ('FRONTEND DEVELOPER', 'Frontend Developer'), ('ADMINISTRATIVE ASSISTANT', 'Administrative Assistant'), ('RECEPTIONIST', 'Receptionist'), ('OFFICE MANAGER', 'Office Manager'), ('AUDITING CLERK', 'Auditing Clerk'), ('BOOKKEEPER', 'Bookkeeper'), ('ACCOUNT EXECUTIVE', 'Account Executive'), ('BRANCH MANAGER', 'Branch Manager'), ('BUSINESS MANAGER', 'Business Manager'), ('QUALITY CONTROL COORDINATOR', 'Quality Control Coordinator'), ('ADMINISTRATIVE MANAGER', 'Administrative Manager'), ('HUMAN RESOURCES', 'Human Resources'), ('OFFICE ASSISTANT', 'Office Assistant'), ('SECRETARY', 'Secretary'), ('ACCOUNT COLLECTOR', 'Account Collector')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='title',
            field=models.CharField(choices=[('MARKETING SPECIALIST', 'Marketing Specialist'), ('MARKETING MANAGER', 'Marketing manager'), ('MARKETING DIRECTOR', 'Marketing Director'), ('GRAPHIC DESIGNER', 'Graphic Designer'), ('MARKETING RESEARCH ANALYST', 'Marketing Research Analyst'), ('MARKETING COMMUNICATIONS MANAGER', 'Marketing Communications Manager'), ('MARKETING CONSULTAN', 'Marketing Consultant'), ('PRODUCT MANAGER', 'Product Manager'), ('PUBLIC RELATIONS', 'Public Relations'), ('SOCIAL MEDIA ASSISTANT', 'Social Media Assistant'), ('BRAND MANAGER', 'Brand Manager'), ('SEO MANAGER', 'Seo Manager'), ('CONTENT MARKETING MANAGER', 'Content Marketing Manager'), ('MEDIA BUYER', 'Media Buyer'), ('DIGITAL MARKETING MANAGER', 'Digital Marketing Manager'), ('ECOMMERCE MARKETING SPECIALIST', 'Ecommerce Marketing Specialist'), ('BRAND STRATEGIST', 'Brand Strategist'), ('MEDIA RELATIONS COORDINATOR', 'Media Relations Coordinator'), ('IT PROFESSIONAL', 'IT Professional'), ('UX DESIGNER & UI DEVELOPER', 'UI Designer & UI Developer'), ('SQL DEVELOPER', 'SQL Developer'), ('WEB DESIGNER', 'Web Designer'), ('WEB DEVELOPER', 'Web Developer'), ('HELP DESK WORKER/DESKTOP SUPPORT', 'Help Desk Worker/desktop Support'), ('SOFTWARE ENGINEER', 'Software Engineer'), ('DATA ENTRY', 'Data Entry'), ('COMPUTER PROGRAMMER', 'Computer Programmer'), ('NETWORK ADMINISTRATOR', 'Network Administrator'), ('ARTIFICIAL INTELLIGENCE ENGINEER', 'Artificial Intelligence Engineer'), ('IT MANAGER', 'IT Manager'), ('TECHNICAL SPECIALIST', 'Technical Specialist'), ('APPLICATION DEVELOPER', 'Application Developer'), ('BACKEND DEVELOPER', 'Backend Developer'), ('FRONTEND DEVELOPER', 'Frontend Developer'), ('ADMINISTRATIVE ASSISTANT', 'Administrative Assistant'), ('RECEPTIONIST', 'Receptionist'), ('OFFICE MANAGER', 'Office Manager'), ('AUDITING CLERK', 'Auditing Clerk'), ('BOOKKEEPER', 'Bookkeeper'), ('ACCOUNT EXECUTIVE', 'Account Executive'), ('BRANCH MANAGER', 'Branch Manager'), ('BUSINESS MANAGER', 'Business Manager'), ('QUALITY CONTROL COORDINATOR', 'Quality Control Coordinator'), ('ADMINISTRATIVE MANAGER', 'Administrative Manager'), ('HUMAN RESOURCES', 'Human Resources'), ('OFFICE ASSISTANT', 'Office Assistant'), ('SECRETARY', 'Secretary'), ('ACCOUNT COLLECTOR', 'Account Collector')], max_length=100),
        ),
    ]
