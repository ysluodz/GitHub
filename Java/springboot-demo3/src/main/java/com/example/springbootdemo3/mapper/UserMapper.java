package com.example.springbootdemo3.mapper;

import com.example.springbootdemo3.domain.Users;
import org.apache.ibatis.annotations.*;

import java.util.List;

@Mapper
public interface UserMapper {

    @Select(value = {"select * from users where username = #{userName}"})
    Users getUserInfo(String userName);

    @Select(value = {"select * from users"})
    @Results({ @Result(column = "userName",property = "userName"), @Result(column = "password", property = "password"), @Result(column = "enabled", property = "enabled")})
    List<Users> getAllUserInfo();


    @Select(value = "insert into users(userName,password,enabled) values(#{userName},#{password},#{enabled})")
    Users addUser(@Param("userName") String id, @Param("password") String age, @Param("enabled") int name);

}
