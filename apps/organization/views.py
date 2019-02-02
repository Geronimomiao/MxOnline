from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import CourseOrg, CityDict
from .forms import UserAskForm

# Create your views here.

class OrgView(View):
    '''
    课程机构列表功能
    '''

    def get(self, request):
        '''
        取出 列表业需要字段
        '''
        all_orgs = CourseOrg.objects.all()
        # -click_nums 倒序排列
        hot_orgs = all_orgs.order_by('-click_nums')[:3]

        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        ct = request.GET.get('ct', '')
        if ct:
            all_orgs = all_orgs.filter(category=ct)

        sort = request.GET.get('sort', '')
        if sort == 'students':
            all_orgs = all_orgs.order_by('-students')
        elif sort == 'courses':
            all_orgs = all_orgs.order_by('-course_nums')

        # 对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # 5 每页的数量
        p = Paginator(all_orgs, 3, request=request)
        orgs = p.page(page)
        all_citys = CityDict.objects.all()
        org_nums = all_orgs.count()

        return render(request, 'org-list.html', {
            "all_orgs": orgs,
            "all_citys": all_citys,
            "org_nums": org_nums,
            'city_id': city_id,
            'ct': ct,
            'hot_orgs': hot_orgs,
            'sort': sort
        })


class AddUserAskView(View):
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)
            return HttpResponse('{"status": "success"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "fail", "msg": "添加出错"}', content_type='application/json')
