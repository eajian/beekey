import xadmin
from xadmin import views
from .models import basicModel, bannerModel, newsModel



class GlobalSettings(object):
    site_title = "Beeky后台管理"
    site_footer = "Beeky后台管理"
    # menu_style = "accordion"

xadmin.site.register(views.CommAdminView, GlobalSettings)



class basicAdmin(object):
    list_display = ['name', "companyName", "update_time", "add_time"]
    model_icon = 'fa fa-empire'

xadmin.site.register(basicModel, basicAdmin)

class bannerAdmin(object):
    list_display = ["index", 'name', "state", "update_time", "add_time"]
    list_editable = ["index", "state"]
    ordering = ('index',)
    model_icon = 'fa fa-picture-o'

xadmin.site.register(bannerModel, bannerAdmin)

class newsAdmin(object):
    list_display = ["name", 'is_hot', "time"]
    list_editable = ["name", "is_hot", "time"]
    ordering = ('id',)
    model_icon = 'fa fa-newspaper-o'

xadmin.site.register(newsModel, newsAdmin)