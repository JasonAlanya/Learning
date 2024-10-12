package com.pharmacy.store.services;

import com.pharmacy.store.repositories.StoreRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class StoreServices {

    @Autowired
    StoreRepository storeRepository;


}
