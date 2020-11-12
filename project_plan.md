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
    

