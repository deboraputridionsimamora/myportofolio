from rest_framework.permissions import BasePermission, SAFE_METHODS


# dipakai di endpoint yang cuma boleh diubah pemilik (superuser)
class IsPortfolioOwnerOrReadOnly(BasePermission):
    message = "Hanya pemilik portofolio yang dapat mengubah data ini."

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_superuser


# dipakai di endpoint yang Editor juga boleh ubah (PUT/PATCH),
# tapi cuma pemilik yang boleh create/delete - sama kayak aturan Tugas 4
class IsPortfolioOwnerOrEditorOrReadOnly(BasePermission):
    message = "Hanya pemilik atau editor yang dapat mengubah data ini."

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        return (
            request.method in ("PUT", "PATCH")
            and request.user.groups.filter(name="Editor").exists()
        )