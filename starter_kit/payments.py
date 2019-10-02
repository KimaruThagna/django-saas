import razorpay,os

client = razorpay.Client(auth=(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET']))