import pika
import csv
import time
import random

# RabbitMQ server configuration
rabbitmq_host = "localhost"  # Replace with your RabbitMQ server host
queue_name = "character_queue"  # Change to your desired queue name

# Function to format the message
def format_message(character_id, character_name):
    return f"{character_id}: {character_name}"

# Function to read CSV and send messages to RabbitMQ
def send_messages():
    try:
        # Create a blocking connection to the RabbitMQ server
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
        channel = connection.channel()

        # Declare a queue (create if not exists)
        channel.queue_declare(queue=queue_name)

        # Read the CSV file
        with open('C:\\Users\\Kim\\Desktop\\Homework\\GradSchool\\44671-80\\streaming-03-bonus-KimLeach\\batchfile_HP_characters.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            
            # Loop through each row in the CSV
            for row in reader:
                character_id = row['Character_ID']
                character_name = row['Character_Name']

                # Format the message
                message = format_message(character_id, character_name)

                # Send the message to the RabbitMQ queue
                channel.basic_publish(exchange='', routing_key=queue_name, body=message)

                print(f"Sent: {message}")

                # Sleep for 1-3 seconds
                time.sleep(random.randint(1, 3))

    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()

if __name__ == "__main__":
    send_messages()
