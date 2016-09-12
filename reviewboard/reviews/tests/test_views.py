    """Tests for views in reviewboard.reviews.views."""

        self.siteconfig.set('auth_require_sitewide_login', False)
        comment_text_1 = 'Comment text 1'
        comment_text_2 = 'Comment text 2'
        comment_text_3 = 'Comment text 3'
        """Testing review_detail and ordering of general comments on a review
        comment_text_1 = 'Comment text 1'
        comment_text_2 = 'Comment text 2'
        comment_text_3 = 'Comment text 3'
        """Testing visibility of file attachments on review requests"""
        comment_text_1 = 'Comment text 1'
        comment_text_2 = 'Comment text 2'
        """Testing visibility of screenshots on review requests"""
        comment_text_1 = 'Comment text 1'
        comment_text_2 = 'Comment text 2'
        self.siteconfig.set('auth_require_sitewide_login', True)
            print('Error: %s' % self._get_context_var(response, 'error'))
            print('Error: %s' % self._get_context_var(response, 'error'))
        user = User.objects.get(username='doc')
        """Testing /diff/raw/ multiple Content-Disposition issue"""
        self.create_diffset(review_request=review_request, name='test, comma')
    def _get_context_var(self, response, varname):
        for context in response.context:
            if varname in context:
                return context[varname]

        return None
