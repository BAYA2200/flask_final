from . import views

from . import app

app.add_url_rule("/", view_func=views.index, methods=["GET"], endpoint="index")
app.add_url_rule("/register", view_func=views.register, methods=["POST", "GET"], endpoint="register")
app.add_url_rule("/login", view_func=views.login, methods=["POST", "GET"], endpoint="login")
app.add_url_rule("/post/add", view_func=views.post_add, methods=["POST", "GET"], endpoint="post_add")
app.add_url_rule("/post/<int:post_id>/delete", view_func=views.post_delete, methods=["GET"], endpoint="post_delete")
app.add_url_rule("/post/<int:post_id>", view_func=views.post_detail, methods=["GET"], endpoint="post_detail")
app.add_url_rule("/logout", view_func=views.logout, methods=["POST", "GET"], endpoint="logout")