package com.pharmacy.store.entity;

import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity
@Table(name="tbl_pharmacy_store")
public class Store {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long studentId;

    @Column(nullable = false)
    private String name;

    @Column(name = "phone_number",nullable = false)
    private String phoneNumber;

    @Column(nullable = false)
    private String address;

    private String email;

}
