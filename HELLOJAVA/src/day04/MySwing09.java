package day04;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing09 extends JFrame {

	private JPanel contentPane;
	private JTextField tf_first;
	private JTextField tf_last;
	private JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing09 frame = new MySwing09();
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
	public MySwing09() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 223, 510);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl_first = new JLabel("첫별수");
		lbl_first.setBounds(12, 13, 57, 15);
		contentPane.add(lbl_first);
		
		JLabel lbl_last = new JLabel("끝별수");
		lbl_last.setBounds(12, 38, 57, 15);
		contentPane.add(lbl_last);
		
		tf_first = new JTextField();
		tf_first.setBounds(81, 10, 116, 21);
		contentPane.add(tf_first);
		tf_first.setColumns(10);
		
		tf_last = new JTextField();
		tf_last.setBounds(81, 35, 116, 21);
		contentPane.add(tf_last);
		tf_last.setColumns(10);
		
		JButton btn = new JButton("별출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btn.setBounds(12, 66, 97, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(12, 99, 185, 362);
		contentPane.add(ta);
	}

	public void myClick() {
		String star ="";
		String txt ="";
		String first = tf_first.getText();
		int ifirst = Integer.parseInt(first);
		String last = tf_last.getText();
		int ilast= Integer.parseInt(last);
		
		for(int i = 0; i< ifirst; i++) {
			star +="*";
		}
		System.out.println(star);
		for(int i = ifirst; i<ilast; i++) {
			txt+=star+"\n";
			star+="*";
		}
		ta.setText(txt);
		
		
	}
//쌤 방식~	
	public void mycick() {
		String f = tf_first.getText();
		String l = tf_last.getText();
		String txt ="";
		int ff = Integer.parseInt(f);
		int ll = Integer.parseInt(l);
		for(int i = ff; i<=ll;i++) {
			txt += drawStar(i);
		}
		
		ta.setText(txt);
	}

	public String drawStar(int cnt) {
		String ret ="";
		for(int i = 0; i<cnt; i++) {
			ret += "*";
		}
		ret +="\n";
		return ret;
	}

//~쌤 방식	


}
