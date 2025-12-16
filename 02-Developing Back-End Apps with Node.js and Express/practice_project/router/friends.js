const express = require('express');

const router = express.Router();

let friends = {
    "johnsmith@gamil.com": {"firstName": "John","lastName": "Doe","DOB":"22-12-1990"},
    "annasmith@gamil.com":{"firstName": "Anna","lastName": "smith","DOB":"02-07-1983"},
    "peterjones@gamil.com":{"firstName": "Peter","lastName": "Jones","DOB":"21-03-1989"}
};


// GET request: Retrieve all friends
router.get("/",(req,res)=>{
  res.send(JSON.stringify(friends, null, 4));
});

// GET by specific ID request: Retrieve a single friend with email ID
router.get("/:email",(req,res)=>{
  //Extract email from request parameters
  const email = req.params.email;

  //Return friend datails for the given email
  res.send(friends[email]);
});

// POST request: Add a new friend
router.post("/", function(req, res) {
    // Check if email is provided in the request body
    if (req.body.email) {
        // Create or update friend's details based on provided email
        friends[req.body.email] = {
            "firstName": req.body.firstName,
            "lastName": req.body.lastName,
            "DOB": req.body.DOB
        };
    }
    // Send response indicating user addition
    res.send("The user" + (' ') + (req.body.firstName) + " Has been added!");
});

router.put("/:email", function(req, res) {
    // Extract email parameter from request URL
    const email = req.params.email;
    let friend = friends[email];  // Retrieve friend object associated with email

    if (friend) {  // Check if friend exists
      let DOB = req.body.DOB;
      let firstName = req.body.firstName;
      let lastName = req.body.lastName;  

        // Update DOB if provided in request body
        if (DOB) {
            friend["DOB"] = DOB;
        }

        // Update firstName if provided in request body
        if (firstName) {
          friend["firstName"] = firstName;
        }

        //Update lastName if provided in request body
        if (lastName) {
          friend["lastName"] = lastName;
        }

        friends[email] = friend;  // Update friend details in 'friends' object
        res.send(`Friend with the email ${email} updated.`);
    } else {
        // Respond if friend with specified email is not found
        res.send("Unable to find friend!");
    }
});


// DELETE request: Delete a friend by email id
router.delete("/:email", (req, res) => {
  // Extract the email parameters from the request
  const email = req.params.email;
  // Dalete the friend from the friends object using the email as the key
  if (email){
    delete friends[email];
  }
  // Send response indicating user has been deleted
  res.send(`Friend with the email ${email} deleted.`);
});

module.exports=router;
