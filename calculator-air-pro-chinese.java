import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class CalculatorGUI extends JFrame {
    private JTextField numField1;
    private JTextField numField2;
    private JLabel resultLabel;

    public CalculatorGUI() {
        setTitle("简易计算器");
        setSize(300, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        JPanel mainPanel = new JPanel();
        mainPanel.setLayout(new GridLayout(4, 2, 10, 10));

        JLabel numLabel1 = new JLabel("第一个数字：");
        numField1 = new JTextField();
        JLabel numLabel2 = new JLabel("第二个数字：");
        numField2 = new JTextField();

        JLabel operatorLabel = new JLabel("操作选择：");
        JComboBox<String> operatorComboBox = new JComboBox<>(new String[]{"加法", "减法", "乘法", "除法"});

        JButton calculateButton = new JButton("计算");
        resultLabel = new JLabel("结果：");

        calculateButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                double num1 = Double.parseDouble(numField1.getText());
                double num2 = Double.parseDouble(numField2.getText());
                String operator = (String) operatorComboBox.getSelectedItem();
                double result = 0;

                switch (operator) {
                    case "加法":
                        result = num1 + num2;
                        break;
                    case "减法":
                        result = num1 - num2;
                        break;
                    case "乘法":
                        result = num1 * num2;
                        break;
                    case "除法":
                        if (num2 != 0) {
                            result = num1 / num2;
                        } else {
                            resultLabel.setText("结果：除数不能为零！");
                            return;
                        }
                        break;
                }

                resultLabel.setText("结果：" + result);
            }
        });

        mainPanel.add(numLabel1);
        mainPanel.add(numField1);
        mainPanel.add(numLabel2);
        mainPanel.add(numField2);
        mainPanel.add(operatorLabel);
        mainPanel.add(operatorComboBox);
        mainPanel.add(calculateButton);
        mainPanel.add(resultLabel);

        add(mainPanel);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            CalculatorGUI calculatorGUI = new CalculatorGUI();
            calculatorGUI.setVisible(true);
        });
    }
}
