package com.example.springbootdemo4;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@SpringBootApplication
public class SpringbootDemo4Application {

	public static void main(String[] args) {

		SpringApplication.run(SpringbootDemo4Application.class, args);
	}

	@RequestMapping("/")
	public String Hello(){
		return "Hello, Spring Boot...";
	}

}
