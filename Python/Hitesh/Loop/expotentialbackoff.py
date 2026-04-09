import time

wait_time = 1  # Initial wait time in seconds
max_retry = 5  # Maximum number of retries


for attempt in range (1, max_retry + 1):
   try:
      print(f"Attempt {attempt}: Trying To Connect...")
      raise Exception("Connection Failed")  # Simulating a connection failure
   except Exception as e:
        print(f"Attempt {attempt} failed: {e}")
        if attempt < max_retry:
            print(f"Waiting for {wait_time} seconds before retrying...")
            time.sleep(wait_time)
            wait_time *= 2  # Exponentially increase the wait time
        else:
            print("Max retries reached. Could not establish a connection.")