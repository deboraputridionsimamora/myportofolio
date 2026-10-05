from django.urls import path

from main.views import (
    show_main,
    show_experience,
    show_certification,
    create_certification,
    create_certification_ajax,
    update_certification,
    delete_certification,
    delete_certification_ajax,
    get_certifications_json,
    toggle_star,
    toggle_star_ajax,
    register,
    login_user,
    logout_user,
    certification_list_htmx,
    toggle_star_htmx,
    create_certification_htmx,
    delete_certification_htmx,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("certification/", show_certification, name="show_certification"),
    path("certification/add/", create_certification, name="create_certification"),
    path("certification/add-ajax/", create_certification_ajax, name="create_certification_ajax"),
    path("certification/<int:id>/update/", update_certification, name="update_certification"),
    path("certification/<int:id>/delete/", delete_certification, name="delete_certification"),
    path("certification/<int:id>/delete-ajax/", delete_certification_ajax, name="delete_certification_ajax"),
    path("certification/<int:id>/star/", toggle_star, name="toggle_star"),
    path("certification/<int:id>/star-ajax/", toggle_star_ajax, name="toggle_star_ajax"),
    path("api/certifications/", get_certifications_json, name="get_certifications_json"),
    # Tutorial 6: url khusus HTMX (balesannya potongan HTML)
    path("certification/htmx/list/", certification_list_htmx, name="certification_list_htmx"),
    path("certification/htmx/add/", create_certification_htmx, name="create_certification_htmx"),
    path("certification/<int:id>/htmx/star/", toggle_star_htmx, name="toggle_star_htmx"),
    path("certification/<int:id>/htmx/delete/", delete_certification_htmx, name="delete_certification_htmx"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]