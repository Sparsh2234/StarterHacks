package com.example.health_app;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.Statement;
import java.sql.SQLException;

public class MainActivity extends AppCompatActivity
{

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void store_input(View view)
    {

        EditText et = findViewById(R.id.input);
        String st = et.getText().toString();
        upload_data(st);
    }

    public void upload_data(String st)
    {
        String driver="com.mysql.jdbc.Driver";
        String url="jdbc:mysql://10.32.58.85:3306/mydb";
        String uname="sparsh";
        String pass="password";
        try
        {
            Class.forName(driver);
        }
        catch (ClassNotFoundException ex)
        {

        }
        try
        {
            Connection c=(Connection) DriverManager.getConnection(url,uname,pass);
            Statement s=c.createStatement();
            s.execute("INSERT INTO mydb.users (id, age, stress_level, education-num, marital-status, occupation, capital gain, capital  loss, hours, native country, gender, ethnic group) VALUES ('66', '121', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1')");
//            String stuff = "INSERT INTO `mydb`.`users` (`id`, `age`, `stress_level`, `education-num`, `marital-status`, `occupation`, `capital gain`, `capital  loss`, `hours`, `native country`, `gender`, `ethnic group`) VALUES ('6', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1');"
//                    "" +
//                    "INSERT INTO users (age)" + "values (?)";
//            PreparedStatement pstmt = c.prepareStatement(stuff);
//            pstmt.setString(1, st);
//            pstmt.setString(1, st);
//            pstmt.setString(1, st);
//            pstmt.setString(1, st);
//            pstmt.setString(1, st);
//            pstmt.setString(1, st);
//            pstmt.setString(1, st);
//            pstmt.setString(1, st);
//            pstmt.setString(1, st);

//            pstmt.execute();
        }
        catch (java.sql.SQLException ex)
        {

        }

    }
}
