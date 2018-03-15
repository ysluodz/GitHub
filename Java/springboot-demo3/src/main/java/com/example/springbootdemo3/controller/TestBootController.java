package com.example.springbootdemo3.controller;

import com.example.springbootdemo3.domain.Users;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@EnableAutoConfiguration
@RequestMapping("/testboot")
public class TestBootController {



    @RequestMapping("/getuser")
    public Users getUser(){
        Users user = new Users();
        user.setPassword("good luck");
        return user;
    }

}
