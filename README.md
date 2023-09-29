# API Endpoints                           Permissions

#Authentication
domain/api/v1/auth/login                Any
domain/api/v1/auth/logout               Authorized
domain/api/v1/auth/register             Any
domain/api/v1/auth/register-staff       Admin
domain/api/v1/auth/sent-otp             Any
domain/api/v1/auth/verify-otp           Any

# Profile
domain/api/v1/profile                   Authorized

# Bookings
domain/api/v1/bookings                  Authorized
domain/api/v1/book-confirm              Authorized
domain/api/v1/book-success              Authorized
domain/api/v1/book-cancel               Authorized

# Notifications
domain/api/v1/notification              Authorized
domain/api/v1/notification/create       Admin
domain/api/v1/notification/send         Admin
domain/api/v1/notification/delete       Admin

# Gallery
domain/api/v1/gallery                   Any
domain/api/v1/gallery/add               Admin
domain/api/v1/gallery/delete            Admin

# Staffs
domain/api/v1/staffs                    Any

# Services
domain/api/v1/staff/services                  Any
domain/api/v1/staff/services/add              Admin
domain/api/v1/staff/services/delete           Admin
domain/api/v1/staff/services/update           Admin

# Subservices
domain/api/v1/staff/services/sub-services                   Any
domain/api/v1/staff/services/sub-services/add               Admin
domain/api/v1/staff/services/sub-services/delete            Admin
domain/api/v1/staff/services/sub-services/update            Admin

# Schedule
domain/api/v1/staff/services/sub-services                   Any
domain/api/v1/staff/services/sub-services/add               Admin
domain/api/v1/staff/services/sub-services/delete            Admin
domain/api/v1/staff/services/sub-services/update            Admin

# Schedule
domain/api/v1/staff/schedule            Any

# Schedule-Shop
domain/api/v1/shoptiming                Any

# About Us
domain/api/v1/about-us                  Any

# Partnerships
domain/api/v1/partnerships              Any
domain/api/v1/partnership/add           Admin
domain/api/v1/partnership/remove        Admin
