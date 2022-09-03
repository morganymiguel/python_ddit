package day04;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing03 extends JFrame {

	private JPanel contentPane;
	private JTextField tfA;
	private JTextField tfB;
	private JTextField tfC;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing03 frame = new MySwing03();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing03() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tfA = new JTextField();
		tfA.setBounds(12, 29, 50, 21);
		contentPane.add(tfA);
		tfA.setColumns(10);
		
		tfB = new JTextField();
		tfB.setColumns(10);
		tfB.setBounds(119, 29, 50, 21);
		contentPane.add(tfB);
		
		tfC = new JTextField();
		tfC.setColumns(10);
		tfC.setBounds(276, 29, 50, 21);
		contentPane.add(tfC);
		
		JLabel lbl = new JLabel("*");
		lbl.setBounds(82, 32, 25, 15);
		contentPane.add(lbl);
		
		JButton btn = new JButton("=");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.setBounds(181, 28, 64, 23);
		contentPane.add(btn);
	}
	
	public void myclick() {
		String a = tfA.getText();
		String b = tfB.getText();
		
		int aa = Integer.parseInt(a);
		int bb = Integer.parseInt(b);
		
		int sum = aa + bb;
		
		tfC.setText(sum+"");
		
		
	}

}






















