package com.example.springbootdemo3.service;

import com.example.springbootdemo3.domain.Users;
import com.example.springbootdemo3.mapper.UserMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service("userService")
public class UserService {

    @Autowired
    private UserMapper userMapper;

    public Users getUserInfo(String userName){
        return userMapper.getUserInfo(userName);
    }

    public List<Users> getAllUserInfo(){
        return userMapper.getAllUserInfo();
    }

    @Transactional
    public Users addUser(String userName,String password,int enabled){
        return userMapper.addUser(userName, password, enabled);
    }

    @Transactional
    public Users insert(String userName,String password,int enabled){
        return userMapper.insert(userName, password, enabled);
    }
}
