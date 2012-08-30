# Create your views here.
def sponsors(request,domain,num):
  event = get_event(domain,num)
	sponsors = Sponsor.objects.filter(event = event)

	return render_to_response(url +'sponsors.html',{'name':'Sponsors','list':create_events_menu(event),'event':event,'sponsors':sponsors},context_instance=RequestContext(request))