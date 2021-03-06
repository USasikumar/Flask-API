
#This file containes all the test cases. The pytest module is used to test flask application test cases

from blog_posts import app

class TestClass:
    def test_one(self):  #test case to check if response is same as when tags=history
        response = app.test_client().get('/api/posts?tags=history')

        assert response.status_code == 200
        assert response.data == b'{"posts":[{"author":"Ahmad Dunn","authorId":7,"id":100,"likes":573,"popularity":0.43,"reads":89894,"tags":["science","design","history"]},{"author":"Lainey Ritter","authorId":1,"id":96,"likes":395,"popularity":0.44,"reads":99575,"tags":["science","history"]},{"author":"Jon Abbott","authorId":4,"id":95,"likes":985,"popularity":0.42,"reads":55875,"tags":["politics","tech","health","history"]},{"author":"Trevon Rodriguez","authorId":5,"id":93,"likes":881,"popularity":0.41,"reads":73964,"tags":["tech","history"]},{"author":"Adalyn Blevins","authorId":11,"id":89,"likes":251,"popularity":0.6,"reads":75503,"tags":["politics","startups","tech","history"]},{"author":"Kinley Crosby","authorId":10,"id":88,"likes":371,"popularity":0.35,"reads":21916,"tags":["culture","science","history"]},{"author":"Ahmad Dunn","authorId":7,"id":86,"likes":873,"popularity":0.91,"reads":53869,"tags":["startups","history"]},{"author":"Rylee Paul","authorId":9,"id":84,"likes":233,"popularity":0.65,"reads":17854,"tags":["politics","tech","history"]},{"author":"Bryson Bowers","authorId":6,"id":81,"likes":552,"popularity":0.09,"reads":22975,"tags":["design","history"]},{"author":"Lainey Ritter","authorId":1,"id":80,"likes":874,"popularity":0.47,"reads":9002,"tags":["politics","history"]},{"author":"Kinley Crosby","authorId":10,"id":79,"likes":617,"popularity":0.07,"reads":52494,"tags":["culture","startups","history"]},{"author":"Adalyn Blevins","authorId":11,"id":69,"likes":425,"popularity":0.56,"reads":5149,"tags":["science","history"]},{"author":"Trevon Rodriguez","authorId":5,"id":67,"likes":903,"popularity":0.71,"reads":26815,"tags":["health","history"]},{"author":"Trevon Rodriguez","authorId":5,"id":65,"likes":498,"popularity":0.87,"reads":85870,"tags":["history"]},{"author":"Tia Roberson","authorId":2,"id":64,"likes":163,"popularity":0.34,"reads":22095,"tags":["politics","history"]},{"author":"Zackery Turner","authorId":12,"id":50,"likes":898,"popularity":0.96,"reads":4923,"tags":["health","history"]},{"author":"Ahmad Dunn","authorId":7,"id":45,"likes":31,"popularity":0.89,"reads":63432,"tags":["science","history"]},{"author":"Tia Roberson","authorId":2,"id":39,"likes":307,"popularity":0.61,"reads":89454,"tags":["politics","history"]},{"author":"Tia Roberson","authorId":2,"id":38,"likes":105,"popularity":0.45,"reads":45896,"tags":["design","history"]},{"author":"Adalyn Blevins","authorId":11,"id":37,"likes":107,"popularity":0.55,"reads":35946,"tags":["tech","health","history"]},{"author":"Jaden Bryant","authorId":3,"id":18,"likes":983,"popularity":0.09,"reads":33952,"tags":["tech","history"]},{"author":"Adalyn Blevins","authorId":11,"id":16,"likes":749,"popularity":0.29,"reads":71754,"tags":["design","history"]},{"author":"Trevon Rodriguez","authorId":5,"id":14,"likes":311,"popularity":0.67,"reads":25644,"tags":["tech","history"]},{"author":"Elisha Friedman","authorId":8,"id":10,"likes":853,"popularity":0.6,"reads":35913,"tags":["science","health","history"]},{"author":"Trevon Rodriguez","authorId":5,"id":8,"likes":735,"popularity":0.76,"reads":8504,"tags":["culture","history"]},{"author":"Zackery Turner","authorId":12,"id":2,"likes":469,"popularity":0.68,"reads":90406,"tags":["startups","tech","history"]}]}\n'

    def test_two(self):  #test case to check if response is same on pinging server
        response = app.test_client().get('/api/ping')

        assert response.status_code == 200
        assert response.data==b'{"success":true}\n'


    def test_three(self):  #test case to check if response is same when tags=history sortBy=id ans direction=asc
        response = app.test_client().get('/api/posts?tags=history&sortBy=id&direction=asc')

        assert response.status_code == 200
        assert response.data==b'{"posts":[{"author":"Zackery Turner","authorId":12,"id":2,"likes":469,"popularity":0.68,"reads":90406,"tags":["startups","tech","history"]},{"author":"Trevon Rodriguez","authorId":5,"id":8,"likes":735,"popularity":0.76,"reads":8504,"tags":["culture","history"]},{"author":"Elisha Friedman","authorId":8,"id":10,"likes":853,"popularity":0.6,"reads":35913,"tags":["science","health","history"]},{"author":"Trevon Rodriguez","authorId":5,"id":14,"likes":311,"popularity":0.67,"reads":25644,"tags":["tech","history"]},{"author":"Adalyn Blevins","authorId":11,"id":16,"likes":749,"popularity":0.29,"reads":71754,"tags":["design","history"]},{"author":"Jaden Bryant","authorId":3,"id":18,"likes":983,"popularity":0.09,"reads":33952,"tags":["tech","history"]},{"author":"Adalyn Blevins","authorId":11,"id":37,"likes":107,"popularity":0.55,"reads":35946,"tags":["tech","health","history"]},{"author":"Tia Roberson","authorId":2,"id":38,"likes":105,"popularity":0.45,"reads":45896,"tags":["design","history"]},{"author":"Tia Roberson","authorId":2,"id":39,"likes":307,"popularity":0.61,"reads":89454,"tags":["politics","history"]},{"author":"Ahmad Dunn","authorId":7,"id":45,"likes":31,"popularity":0.89,"reads":63432,"tags":["science","history"]},{"author":"Zackery Turner","authorId":12,"id":50,"likes":898,"popularity":0.96,"reads":4923,"tags":["health","history"]},{"author":"Tia Roberson","authorId":2,"id":64,"likes":163,"popularity":0.34,"reads":22095,"tags":["politics","history"]},{"author":"Trevon Rodriguez","authorId":5,"id":65,"likes":498,"popularity":0.87,"reads":85870,"tags":["history"]},{"author":"Trevon Rodriguez","authorId":5,"id":67,"likes":903,"popularity":0.71,"reads":26815,"tags":["health","history"]},{"author":"Adalyn Blevins","authorId":11,"id":69,"likes":425,"popularity":0.56,"reads":5149,"tags":["science","history"]},{"author":"Kinley Crosby","authorId":10,"id":79,"likes":617,"popularity":0.07,"reads":52494,"tags":["culture","startups","history"]},{"author":"Lainey Ritter","authorId":1,"id":80,"likes":874,"popularity":0.47,"reads":9002,"tags":["politics","history"]},{"author":"Bryson Bowers","authorId":6,"id":81,"likes":552,"popularity":0.09,"reads":22975,"tags":["design","history"]},{"author":"Rylee Paul","authorId":9,"id":84,"likes":233,"popularity":0.65,"reads":17854,"tags":["politics","tech","history"]},{"author":"Ahmad Dunn","authorId":7,"id":86,"likes":873,"popularity":0.91,"reads":53869,"tags":["startups","history"]},{"author":"Kinley Crosby","authorId":10,"id":88,"likes":371,"popularity":0.35,"reads":21916,"tags":["culture","science","history"]},{"author":"Adalyn Blevins","authorId":11,"id":89,"likes":251,"popularity":0.6,"reads":75503,"tags":["politics","startups","tech","history"]},{"author":"Trevon Rodriguez","authorId":5,"id":93,"likes":881,"popularity":0.41,"reads":73964,"tags":["tech","history"]},{"author":"Jon Abbott","authorId":4,"id":95,"likes":985,"popularity":0.42,"reads":55875,"tags":["politics","tech","health","history"]},{"author":"Lainey Ritter","authorId":1,"id":96,"likes":395,"popularity":0.44,"reads":99575,"tags":["science","history"]},{"author":"Ahmad Dunn","authorId":7,"id":100,"likes":573,"popularity":0.43,"reads":89894,"tags":["science","design","history"]}]}\n'

    def test_four(self): #test case to check if response is same when tags parameter is missing
        response = app.test_client().get('/api/posts')

        assert response.status_code == 400
        assert response.data==b'{"error":"Tags parameter is required"}\n'


    def test_five(self): #test casse to check if response is same when sortby is invalid
        response = app.test_client().get('/api/posts?tags=history&sortBy=test&direction=asc')

        assert response.status_code == 400
        assert response.data==b'{"error":"sortBy parameter is invalid"}\n'

    def test_six(self): #test casse to check if response is same when direction is invalid
        response = app.test_client().get('/api/posts?tags=history&sortBy=id&direction=test')

        assert response.status_code == 400
        assert response.data==b'{"error":"direction parameter is invalid"}\n'