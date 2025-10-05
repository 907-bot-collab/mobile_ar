// Surgery Data for AR Surgery Training System
// Educational content for Laparoscopic Cholecystectomy

const surgerySteps = [
    {
        step: 1,
        title: 'Patient Positioning & Insufflation',
        description: 'Position patient in reverse Trendelenburg. Create pneumoperitoneum with CO2 insufflation to 12-15 mmHg.',
        duration: '10-15 minutes',
        key_points: ['Patient safety', 'Optimal visualization', 'Safe insufflation pressure'],
        instruments: ['Veress needle', 'CO2 insufflator', 'Trocar']
    },
    {
        step: 2,
        title: 'Port Placement & Camera Insertion',
        description: 'Insert 4 trocars: 12mm umbilical (camera), 5mm epigastric, 5mm midclavicular, 5mm anterior axillary.',
        duration: '15-20 minutes',
        key_points: ['Safe trocar insertion', 'Optimal triangulation', 'Injury avoidance'],
        instruments: ['12mm trocar', '5mm trocars', '30° laparoscope']
    },
    {
        step: 3,
        title: 'Calot Triangle Dissection',
        description: 'Dissect Calot triangle to achieve critical view of safety. Identify cystic artery and cystic duct.',
        duration: '20-30 minutes',
        key_points: ['Critical view of safety', 'Avoid bile duct injury', 'Proper dissection plane'],
        instruments: ['Maryland dissector', 'Hook cautery', 'Graspers']
    },
    {
        step: 4,
        title: 'Critical View of Safety',
        description: 'Achieve and confirm critical view: clear Calot triangle, only 2 structures entering gallbladder, liver bed visible.',
        duration: '10-15 minutes',
        key_points: ['Patient safety milestone', 'Injury prevention', 'Proper identification'],
        instruments: ['Dissector', 'Camera for documentation']
    },
    {
        step: 5,
        title: 'Clipping & Cutting',
        description: 'Apply clips to cystic artery and cystic duct. Cut structures after confirming critical view.',
        duration: '10-15 minutes',
        key_points: ['Secure hemostasis', 'Safe cutting', 'Proper clip application'],
        instruments: ['Clip applier', 'Scissors', 'Suction/irrigation']
    },
    {
        step: 6,
        title: 'Gallbladder Dissection & Removal',
        description: 'Dissect gallbladder from liver bed using cautery. Place in extraction bag and remove.',
        duration: '15-25 minutes',
        key_points: ['Hemostasis', 'Specimen integrity', 'Avoid perforation'],
        instruments: ['Hook cautery', 'Extraction bag', 'Graspers']
    }
];

const complications = [
    'Bile duct injury',
    'Vascular injury',
    'Bowel injury',
    'Gallbladder perforation',
    'Port site hernia'
];

const learningObjectives = [
    'Understand laparoscopic anatomy',
    'Master critical view of safety',
    'Recognize danger zones',
    'Practice safe dissection techniques',
    'Learn complication management'
];

const surgeryInfo = {
    name: 'Laparoscopic Cholecystectomy',
    organ: 'Gallbladder',
    description: 'Minimally invasive gallbladder removal surgery',
    duration: '45-90 minutes',
    difficulty: 'Intermediate',
    anatomy: {
        target_organ: 'Gallbladder',
        approach: 'Laparoscopic (4 port technique)',
        key_structures: ['Cystic artery', 'Cystic duct', 'Common bile duct', 'Liver bed'],
        critical_view: 'Calot triangle dissection for critical view of safety'
    }
};

// Export for module systems (optional)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        surgerySteps,
        complications,
        learningObjectives,
        surgeryInfo
    };
}
