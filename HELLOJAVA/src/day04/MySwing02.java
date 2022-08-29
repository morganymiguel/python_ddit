package day04;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.Color;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing02 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing02 frame = new MySwing02();
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
	public MySwing02() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf = new JTextField();
		tf.setBackground(Color.ORANGE);
		tf.setText("100");
		tf.setBounds(40, 52, 168, 27);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("increase");
		btn.addMouseListener(new MouseAdapter() {
			int cnt = Integer.parseInt(tf.getText());
			@Override
			public void mouseClicked(MouseEvent e) {
				cnt++;
//				String i = ;
				tf.setText(Integer.toString(cnt));
			}
		});
		btn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
			}
		});
		btn.setEnabled(true);
		btn.setBackground(Color.ORANGE);
		btn.setToolTipText("");
		btn.setBounds(220, 52, 168, 27);
		contentPane.add(btn);
	}
}
