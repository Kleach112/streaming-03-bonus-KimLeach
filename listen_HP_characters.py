import pika

# Define the callback function to process received messages
def callback(ch, method, properties, body):
    message = body.decode()  # Decode the message from bytes to string
    print(f"Received message: {message}")
    
    # Write the received message to a file
    with open("received_messages.txt", "a") as file:
        file.write(message + "\n")

# Create a connection to the RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# Declare the queue from which the consumer will receive messages
channel.queue_declare(queue="character_queue")  # Replace with your queue name

# Set up the callback to handle incoming messages
channel.basic_consume(queue="character_queue", on_message_callback=callback, auto_ack=True)  # Replace with your queue name

print("Waiting for messages. To exit, press Ctrl+C")

# Start consuming messages
channel.start_consuming()
