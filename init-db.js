db = db.getSiblingDB("userManagementDb");
db.user_flask.drop();

db.user_flask.insertMany([
    { "name": "Fatmanur Eraslan", "email": "fatmanur_eraslan@gmail.com", "department": "Marketing Department", "phone": "05389264015" },
    { "name": "Emine Eraslan", "email": "emine@gmail.com", "department": "Human Resources", "phone": "053645623533" },
    { "name": "Hasan Kaya", "email": "hasan@gmail.com", "department": "Finance Department", "phone": "05073483243" },
    { "name": "Fatih Yıldız", "email": "fatih@gmail.com", "department": "Sales Department", "phone": "0573463733" },
    { "name": "Ahmet Sancak", "email": "ahmet@gmail.com", "department": "Marketing Department", "phone": "0563456343" },
    { "name": "Salih Demir", "email": "salih@gmail.com", "department": "Sales Department", "phone": "05364562374" },
    { "name": "Büşra Ünverdi", "email": "büsra@gmail.com", "department": "Finance Department", "phone": "05232432432" },
    { "name": "Elif Kaya", "email": "elif@gmail.com", "department": "Human Resource Department", "phone": "0532423432" },
    { "name": "Kerem Kurtuluş", "email": "kerem@gmail.com", "department": "Purchase Department", "phone": "05324343243" },
    { "name": "Murat Baran", "email": "murat@gmail.com", "department": "Sales Department", "phone": "05666354533" },
    { "name": "Özge Tekin", "email": "ozge@gmail.com", "department": "Human Resource Department", "phone": "05434332344" }
]);