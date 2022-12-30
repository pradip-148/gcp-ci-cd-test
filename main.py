import webapp2

class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello, this response is from webapp2!. We are testing for ci/cd pipelines with GCP')

app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
], debug=True)