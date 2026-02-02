---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
excerpt: "Curriculum vitae: education, experience, publications, talks, teaching, and supervision."
redirect_from:
  - /resume
---

{% include base_path %}

<div class="cv-download-links" style="margin: 0 0 1rem 0;">
  <a href="{{ '/files/cv.pdf' | relative_url }}" class="btn btn--primary" download>Download CV (PDF)</a>
</div>

Summary
======
PhD candidate at ETRO (VUB) focused on computer vision and AI for autonomous driving and drone navigation, with expertise in detection, multi-object tracking, and VLMs.

Personal data
======
* Location: Brussels, Belgium
* Email: [leandro.dibella@gmail.com](mailto:leandro.dibella@gmail.com)
* GitHub: <https://github.com/leandro-svg>
* Google Scholar: <https://scholar.google.de/citations?user=f7IDHsgAAAAJ&hl=en>
* ORCID: <https://orcid.org/0009-0000-1731-7205>
* LinkedIn: <https://www.linkedin.com/in/leandro-di-bella-62381413b/>
* App: <https://mappx.app>

Education
======
* 2025–2027 (ongoing): Advanced Master in Industrial and Technological Management — Solvay Brussels School
* 2023–Present: PhD in Engineering Sciences (Artificial Intelligence & Computer Vision) — Department of Electronics and Informatics (ETRO), Vrije Universiteit Brussel (VUB)
* 2020–2023: Master Electrical Engineer (Information Technology Systems option) — Bruface Faculty of Engineering (ULB/VUB)
* 2017–2020: Bachelor Engineer — Bruface Faculty of Engineering (ULB/VUB)

Work experience
======
* Founder — Mappx (Aug 2025–Present)
  * Launched Mappx mobile app in Aug 2025
  * Developed full-stack Flutter frontend and FastAPI backend, integrating location-based social sharing with maps and photos
  * Implemented cost-effective backend infrastructure using Azure and Firebase to support scalable user engagement and deployment on the App Store

* Internship — MACQ Mobility (Aug 2022–Oct 2022)
  * Developed and integrated instance segmentation on a Jetson TX2 edge device (Python/C++)

Projects
======
* 2023: Embedded AI — Real-Time Instance Segmentation with TensorRT and ONNX Deployment
  * Implemented and optimized SparseInst and Yolov7 for real-time deployment on NVIDIA edge devices using CUDA TensorRT

Languages
======
* French (Native)
* English (C1)
* Dutch (B1)

Skills
======
* Programming: Python, Flutter, FastAPI, PyTorch, C++, CUDA, TensorRT
* Tools/Platforms: VS Code, Azure Cloud Services, Docker, Firebase, GitHub CI/CD
* Soft skills: Team spirit, ownership/responsibility, comfort zone growth, adaptability

Publications
======
{% assign coral_slug = '2025-coral-reef-fish-identification' %}

{% if site.publication_category %}
  {% for category in site.publication_category %}
### {{ category[1].title }}

<ul>
      {% assign pubs_in_category = site.publications | where: "category", category[0] | sort: "date" | reverse %}

      {% if category[0] == 'manuscripts' %}
        {% for post in pubs_in_category %}
          {% if post.published == false %}
            {% continue %}
          {% endif %}
          {% if post.url contains coral_slug %}
            {% continue %}
          {% endif %}
          {% include archive-single-cv.html %}
        {% endfor %}
        {% for post in pubs_in_category %}
          {% if post.published == false %}
            {% continue %}
          {% endif %}
          {% if post.url contains coral_slug %}
            {% include archive-single-cv.html %}
          {% endif %}
        {% endfor %}
      {% else %}
        {% for post in pubs_in_category %}
          {% if post.published == false %}
            {% continue %}
          {% endif %}
          {% include archive-single-cv.html %}
        {% endfor %}
      {% endif %}

</ul>
  {% endfor %}
{% else %}
  <ul>
    {% assign pubs_sorted = site.publications | sort: 'date' | reverse %}
    {% for post in pubs_sorted %}
      {% include archive-single-cv.html %}
    {% endfor %}
  </ul>
{% endif %}
  
Talks
======
<ul>
  {% for post in site.talks reversed %}
    {% if post.published == false %}{% continue %}{% endif %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}
</ul>
  
Teaching
======
* Teaching Assistant (2.5 years) — Machine Learning and Big Data Processing, Vrije Universiteit Brussel (VUB)
  
Supervision
======
* Supervised 6 Master's theses:
  * Jules Gerard — Automating Coral Reef Fish Family Identification on Video Transects Using a YOLOv8-Based Deep Learning Pipeline
  * Diana Alexandra Sas — Monocular 3D Object Detection with Pyramid Vision Transformer
  * Kyan David — Autonomous Drone Navigation in GNSS-Degraded and Non-Permissive Environments
  * Mohammed Marsour — Pruning and Quantization Strategies for Efficient Camera-Based Object Detection
  * Cristian Vladoiu — Pedestrian Intention Prediction via Vision-Language Action Models
  * Mayur Ashok Sonawane — Object Pose Estimation on Embedded Devices
