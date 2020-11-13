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
        

  
        

