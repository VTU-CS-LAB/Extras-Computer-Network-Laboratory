
/*
UDP Two Way Connection
*/

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.Scanner;

class UdpClientDuplex {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        try {
            // Client listening to Port 1234
            DatagramSocket datagramSocket = new DatagramSocket(1234);
            InetAddress serverAddress = InetAddress.getByName("127.0.0.1");
            byte[] buffer;
            DatagramPacket datagramPacket;
            String msgReceived, msgSent;
            while (true) {

                // Receive the Message from Server and print it to Console
                buffer = new byte[65535];
                datagramPacket = new DatagramPacket(buffer, buffer.length);
                datagramSocket.receive(datagramPacket);
                msgReceived = new String(buffer).trim();
                System.out.print("Message received from Server: ");
                System.out.println(msgReceived);

                // Condition to Exit the Loop
                if (msgReceived.equalsIgnoreCase("exit")) {
                    break;
                }

                // Input the Message From Console and Send it to Client
                System.out.print("Enter Message to send to the Server: ");
                msgSent = scanner.nextLine();
                buffer = msgSent.getBytes();
                datagramPacket = new DatagramPacket(buffer, buffer.length, serverAddress, 1233);
                datagramSocket.send(datagramPacket);

                // Condition to Exit the Loop
                if (msgSent.equalsIgnoreCase("exit")) {
                    break;
                }
            }
            datagramSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
