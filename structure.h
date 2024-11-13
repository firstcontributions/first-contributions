// structure details

struct apple
{
    char name[25]; char specs[50]; int price; 
}; //iPhone[4], MacBook[4], iPad[4], AirPods[4], Apple_watch[3]; 

struct apple iPhone[4] = {
    {"iPhone SE", "Processor: A13 Bionic, Screen Size: 4.7 inches", 30000},
    {"iPhone 11", "Processor: A13 Bionic, Screen Size: 6.1 inches", 37500},
    {"iPhone 12", "Processor: A14 Bionic, Screen Size: 6.1 inches", 45000},
    {"iPhone 13", "Processor: A15 Bionic, Screen Size: 6.1 inches", 52500}
};

struct apple MacBook[4] = {
    {"MacBook Air", "Processor: Apple M1, Screen size: 13.3 inches", 75000},
    {"MacBook Pro 13", "Processor: Apple M1, Screen size: 13.3 inches", 93750},
    {"MacBook Pro 14", "Processor: Apple M1 Pro/Max", 150000},
    {"MacBook Pro 16", "Processor: Apple M1 Pro/Max", 187500}
};

struct apple iPad[4] = {
    {"iPad 9", "Processor: A13 Bionic, Screen size: 10.9 inches", 24750},
    {"iPad Mini", "Processor: A15 Bionic, Screen size: 8.3 inches", 37500},
    {"iPad Pro 11", "Processor: Apple M1, Screen size: 11 inches", 56250},
    {"iPad Pro 12.9", "Processor: Apple M1, Screen size: 12.9 inches", 75000}
};

struct apple AirPods[4] = {
    {"AirPods 2", "Processor: Apple H1 chip, 5 hrs battery life", 9750},
    {"AirPods 3", "Processor: Apple H1 chip, 6 hrs battery life", 13500},
    {"AirPods Pro", "Processor: Apple H1 chip, 4.5 hrs battery life", 18750},
    {"AirPods Max", "Processor: Apple H1 chip, 20 hrs battery life", 41250}
};

struct apple Watch[3] = {
    {"Apple Watch Series 3", "Screen size: 38/42 mm, 18 hrs battery life", 15000},
    {"Apple Watch SE", "Screen size: 40/44 mm, 18 hrs battery life", 21000},
    {"Apple Watch Series 7", "Screen size: 41/45 mm, 18 hrs battery life", 30000}
};

struct apple cart[10];

// struct iPhone[0] = {"iPhone SE", "Processor: A13 Bionic \n Screen Size: 4.7 inches", 30000};
// struct iPhone[1] = {"iPhone 11", "Processor: A13 Bionic \n Screen Size: 6.1 inches", 37500};
// struct iPhone[2] = {"iPhone 12", "Processor: A14 Bionic \n Screen Size: 6.1 inches", 45000};
// struct iPhone[3] = {"iPhone 13", "Processor: 15 Bionic \n Screen Size: 6.1 inches", 52500};

// struct MacBook[0] = {"MacBook Air", "Processor: Apple M1 \n Screen size: 13.3 inches", 75000};
// struct MacBook[1] = {"MacBook Pro 13", "Processor: Apple M1 \n Screen size: 13.3 inches", 93750};
// struct MacBook[2] = {"MacBook Pro 14", "Processor: Apple M1 Pro/Max \n Screen size: 14.2 inches", 150000};
// struct MacBook[3] = {"MacBook Pro 16", "Processor: Apple M1 Pro/Max \n Screen size: 16.2 inches", 187500};

// struct iPad[0] = {"iPad 9", "Processor: A13 Bionic \n Screen size: 10.9 inches", 24750};
// struct iPad[1] = {"iPad Mini", "Processor: A15 Bionic \n Screen size: 8.3 inches", 37500};
// struct iPad[2] = {"iPad Pro 11", "Processor: Apple M1 \n Screen size: 11 inches", 56250};
// struct iPad[3] = {"iPad Pro 12.9", "Processor: Apple M1 \n Screen size: 12.9 inches", 75000};

// struct AirPods[0] = {"AirPods 2", "Processor: Apple H1 chip \n 5 hrs battery life", 9750};
// struct AirPods[1] = {"AirPods 3", "Processor: Apple H1 chip \n 6 hrs battery life", 13500};
// struct AirPods[2] = {"AirPods Pro", "Processor: Apple H1 chip \n 4.5 hrs battery life", 18750};
// struct AirPods[3] = {"AirPods Max", "Processor: Apple H1 chip \n 20 hrs battery life", 41250};

// struct Apple_watch[0] = {"Apple Watch Series 3", "Screen size: 38/42 mm \n 18 hrs battery life", 15000};
// struct Apple_watch[1] = {"Apple Watch SE", "Screen size: 40/44 mm \n 18 hrs battery life", 21000};
// struct Apple_watch[2] = {"Apple Watch Series 7", "Screen size: 41/45 mm \n 18 hrs battery life", 30000};