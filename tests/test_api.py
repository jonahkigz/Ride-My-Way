import unittest
import app
import json



class TestCases(unittest.TestCase):
    def setUp(self):

        self.test_all = app.returnAll()
        self.mock_ride={
            "id": 1 ,
            "from": "Mukono",
            "to": "Arua",
            "time/date": "5/7/2018 10pm",
            
        }
   
    def test_get_rides(self):
        response = self.test_all.get('/api/v1/car')
        self.assertEqual(response.status_code, 200)
    def test_get_one_ride(self):
        response = self.test_all.get('/api/v1/car/<int:Id>')
        self.assertEqual(response.status_code, 200)
    #Test whether a ride created successfully
    def add_ride_offer(self):
        response = self.test_all.get('/api/v1/car',
                                     data=json.dumps(self.mock_ride),
                                     content_type='application/json')
        self.assertEquals(response.status_code,201)
        self.assertEquals(response.get_data()), {"message": "ride created successfully"}

    #if some one tries to submit a blank form
    def adding_blank_form(self):
        new_ride = {}
        response = self.test_all.post('/api/v1/car',
                                 data=json.dumps(new_ride),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
  

        #Test for ride edit, say update number of seats
    def edit_ride_offer(self):
        response = self.test_all.get('/api/v1/car/<int:Id>')
        #self.assertIn('',
                      #self.rides_list[0][])
        #self.assertIn(, self.rides_list)



if __name__ == '__main':
    unittest.main()

     
     

