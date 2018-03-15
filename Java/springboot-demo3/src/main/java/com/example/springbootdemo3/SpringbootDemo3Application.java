package com.example.springbootdemo3;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@MapperScan("com.mapper.*Mapper")
public class SpringbootDemo3Application {

	public static void main(String[] args) {
		SpringApplication.run(SpringbootDemo3Application.class, args);
	}
}
//其中还需要在启动类中加一个注解@MapperScan("com.mapper.*Mapper")，指明在启动的时候加载com.mapper下以Mapper结尾的类。