
/*
UDP Two Way Connection
*/

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.Scanner;

class UdpServerDuplex {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        try {
            // Server Listening to Port 1233
            DatagramSocket datagramSocket = new DatagramSocket(1233);
            InetAddress clientAddress = InetAddress.getByName("127.0.0.1");
            String msgSent, msgReceived;
            byte[] buffer;
            DatagramPacket datagramPacket;
            while (true) {
                // Input the Message From Console and Send it to Client
                System.out.print("Enter Message to send to the Client: ");
                msgSent = scanner.nextLine();
                buffer = msgSent.getBytes();
                datagramPacket = new DatagramPacket(buffer, buffer.length, clientAddress, 1234);
                datagramSocket.send(datagramPacket);

                // Condition to Exit the Loop
                if (msgSent.equalsIgnoreCase("exit")) {
                    break;
                }

                // Receive the Message from Client and print it to Console
                buffer = new byte[65535];
                datagramPacket = new DatagramPacket(buffer, buffer.length);
                datagramSocket.receive(datagramPacket);
                msgReceived = new String(buffer).trim();
                System.out.print("Message Received: ");
                System.out.println(msgReceived);

                // Condition to Exit the Loop
                if (msgReceived.equalsIgnoreCase("exit")) {
                    break;
                }
            }
            datagramSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
