Claims App

- Claims List View

- Claims Detail View

- Claims Create View

- Claims Update


Core App

- Home List View


Staff App

- Claims List View

- Claims Detail View

- Claims Create View

- Claims Update

- Add admin account

- Update Status

- Update Amount Recieved

Fixes

- 404 Errors
- Removing object pk numbers
- Models: Last updated

ClaimsDetailView Old
     def get_object(self):
         claim = super(ClaimsDetailView, self).get_object()
         if not claim.user == self.request.user:
             return redirect('claims:claims')
         else:
             return claim
    


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    cost = models.PositiveIntegerField()
    paid = models.PositiveIntegerField()

class =JobListView(LoginRequiredMixin, generic.ListView):
    model = Job
    template_name = 'job/=job_list.html'
    context_object = '=job_list'
    paginate = 10
    queryset = Job.objects.all()

    def get_queryset(self):
        return Job.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
            context = super(=JobListView, self).get_context_data(**kwargs)
            context['job_count'] = self.get_queryset().count()
        

  
UX Mood Board

https://dribbble.com/shots/9933035-Fintech-web-app-UI-UX-design
https://www.instagram.com/p/B3qpAZJgY0D/

https://www.google.com/search?q=monday.com&tbm=isch&ved=2ahUKEwil07_IufTtAhUTShoKHY-PB2AQ2-cCegQIABAA&oq=monday.com&gs_lcp=CgNpbWcQAzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCABQkCRY0Sdg8SpoAHAAeACAAeABiAGtBpIBBTAuMS4zmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=38nrX-XnA5OUaY-fnoAG&bih=698&biw=1536#imgrc=qEzLnZUPecGOHM
https://www.pcmag.com/reviews/mondaycom

List View
https://dribbble.com/shots/11647076-Gifta-Dashboard/attachments/3269776?mode=media

Profile View
https://dribbble.com/shots/11827239-Clients-and-Meetings

Home Page Illustration
https://storyset.com/illustration/creative-team/pana
https://fontawesome.com/icons/handshake?style=regular
https://fontawesome.com/icons/chart-line?style=solid
https://fontawesome.com/icons/hand-holding-usd?style=solid
https://fontawesome.com/icons/search?style=solid


Login
https://storyset.com/illustration/login/bro
https://fontawesome.com/icons/envelope?style=regular
https://fontawesome.com/icons/lock?style=solid


Dashboard

Plus: https://fontawesome.com/icons/plus?style=solid

Profile: https://fontawesome.com/icons/user?style=regular

Invoice: https://fontawesome.com/icons/file-alt?style=regular

Users: https://fontawesome.com/icons/users?style=solid

Close: https://fontawesome.com/icons/window-close?style=regular

Total Claims: https://fontawesome.com/icons/chart-bar?style=regular

Under Review: https://fontawesome.com/icons/search-dollar?style=solid

In Progress: https://fontawesome.com/icons/spinner?style=solid

Completed: https://fontawesome.com/icons/tasks?style=solid


Claims Detail

Company: https://fontawesome.com/icons/building?style=regular

Email: https://fontawesome.com/icons/envelope?style=regular

Sector: https://fontawesome.com/icons/briefcase?style=solid

Phone: https://fontawesome.com/icons/phone-alt?style=solid

Location: 