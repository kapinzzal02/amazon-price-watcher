# Amazon Price Watcher
#### A simple Python web-scraping script that periodically checks if the price of a product has fallen, and notifies you through Email or Telegram.

I recently finished a Python Basics course, and decided I would try this out as my Capstone project. And I've been eyeing a sleek keyboard on Amazon for a while anyways.

## Let's set it up

 1. The script uses the Requests, lxml and BeautifulSoup libraries. To install them, open up the Command Prompt/Terminal and type: `pip install requests`, `pip install lxml` and `pip install bs4`.
 2. Open the `config.json` file, and fill in the details. Don't include any currency symbols or words in the budget field, just an integer will do. The "interval" field is how often the script will run, and by default it is set to 12 hours (23400 seconds). If you set the interval too low (like 10 seconds), Amazon will blacklist your IP Address. Now choose how you want to be notified, by writing in Email or Telegram. If you chose the Telegram method, skip to Step 6.
 3. Assuming you chose the Email method, first fill in your Email Address. This script currently only works with Gmail, so apologies if you use any other service. 
 4. You'll need an App Password to log in. [Here's how you can set up an App Password with Gmail](https://support.google.com/accounts/answer/185833?hl=en). Remember, you'll need 2-Step Verification on your Google account to do this.
 5. (Optional) If you want to customize the subject and/or the body of the Email, open the Python script with any text editor of your choice and look for the `email_notify()` function. You should see the part where you can edit the subject and body.
 6. Here's what you have to do to set up Telegram notifications. First, make a Telegram account if you haven't already. Download the app on your phone.
 7. Search for *RawDataBot*, and send it a message. It sends you a JSON file. Copy the number adjacent to "id". Not "message_id", not "update_id", just plain old "id". Paste that number into the `config.json` file.
 8. Now search for *BotFather*, which is a bot that allows users to make bots of their own. Click on start, and type `/newbot`. Follow the instructions, and *BotFather* should give you a token). Copy it and paste it in.
 9. You're done! All that's left is to run the script. It will now check the product page at regular intervals, and if it sees that the price is within your budget, it will notify you.

## Limitations

 1. The script currently takes in only one product. To check multiple products at once, you'll have to run the script separately for each. I will update this script soon to fix this, probably by implementing a database of sorts.
 2. As mentioned earlier, the script can only send emails if you have a Gmail account. I'll look into a better solution.
 3. I'm currently running this script on a Raspberry Pi, which stays online 24/7 so I only had to run this script once. If you are running it on a computer, you'll have to run the script every time you boot up. I'll look into implementing the script with cron to fix this (somewhat). **Tip:** Put this script up on [PythonAnywhere](https://www.pythonanywhere.com/).

Thanks for taking a look. This is the first project I have ever made, so it's rough around the edges. But hey, it gets the job done. 😉
 