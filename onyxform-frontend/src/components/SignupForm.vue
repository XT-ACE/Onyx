<template>
  <div class="onyx-form">
    <div class="form-container">
      <div class="onyx-header">
        <h1>CF - ONYX MEMBERSHIP CARD APPLICATION FORM</h1>
        <p>
          The following personalities are NOT ALLOWED to register and/or play in this casino:
        </p>
        <ul>
          <li>♠️ <strong>Government Official</strong> or employee connected directly with the operation of the <strong>Government</strong> or any of its agencies.</li>
          <li>♠️ Member of the <strong>Armed Forces of the Philippines</strong>, including the Army, Navy, Air Force, or the Philippine National Police.</li>
          <li>♠️ Persons <strong>under 21</strong> years of age.</li>
          <li>♠️ Persons included in the PAGCOR's National Database of Restricted Persons (<strong>NDRP</strong>).</li>
          <li>♠️ Gaming Employment License (<strong>GEL</strong>) holder.</li>
          <li>Funds or credits in the account of player who is found ineligible to play shall mean forfeiture of said funds/credits in favor of the Government.</li>
        </ul>
        
      </div>

      <div class="progress-bar">
        <div :class="{ active: currentStep >= 1 }">1</div>
        <div :class="{ active: currentStep >= 2 }">2</div>
        <div :class="{ active: currentStep >= 3 }">3</div>
        <div :class="{ active: currentStep >= 4 }">4</div>
      </div>

      <form @submit.prevent="submitForm" class="form">

        <!-- Step 1: Consent -->
        <div v-if="currentStep === 1">
          <h2>Step 1: Consent</h2>
          <div class="form-consents">
            <p>By proceeding, you confirm that you have read, understood, and agree to abide by the Casino Filipino - Onyx Casino</p>
            <div>
              <input v-model="formData.agreeToPrivacy" type="checkbox" />
              <label>
                I agree to the 
                <a href="https://www.pagcor.ph/docs/data-privacy-notice.pdf" target="_blank">
                  Privacy Statement
                </a>
              </label>
              <span v-if="!formData.agreeToPrivacy && showErrors" class="error-message">
                This is a required field
              </span>
            </div>
            <div>
              <input v-model="formData.isOver21" type="checkbox" />
              <label> I agree to the <a href="https://www.pagcor.ph/regulatory/pdf/RG-Code-of-Practice-v6.pdf" target="_blank">
                  Terms and Conditions
                </a></label>
              <span v-if="!formData.isOver21 && showErrors" class="error-message">
                This is a required field
              </span>
            </div>
          </div>
          <button @click="nextStep">Next</button>
        </div>

        <!-- Step 2: Personal Information -->
        <div class="personal-info" v-if="currentStep === 2">
          <h2>Step 2: Personal Information</h2>
          <select v-model="formData.title">
            <option value="" disabled>Title</option>
            <option value="Mr">Mr</option>
            <option value="Mrs">Mrs</option>
            <option value="Ms">Ms</option>
          </select>
          <input v-model="formData.last_name" placeholder="Enter your last name" required />
          <input v-model="formData.first_name" placeholder="Enter your first name" required />
          <input v-model="formData.age" type="number" placeholder="Age" required />
          <span v-if="formData.age && formData.age < 21" class="error-message">
            You must be 21 or older
          </span>
          <div class="dropdown" ref="dropdown">
    <input
      type="text"
      v-model="formData.nationality"
      placeholder="Search Nationality"
      @focus="isOpen = true"
      @input="filterNationalities"
    />
    <ul v-if="isOpen" class="dropdown-menu">
      <li
        v-for="(item, index) in filteredNationalities"
        :key="index"
        @click="selectNationality(item.name)"
      >
        {{ item.name }}
      </li>
    </ul>
  </div>
  <div class="personal-info-btn">
    <button @click="prevStep">Back</button>
    <button @click="nextStep">Next</button>
  </div>
  </div>
        <!-- Step 3: Contact Information -->
        <div class="contact-info" v-if="currentStep === 3">
    <h2>Step 3: Contact Information</h2>
    <div class="country-code-wrapper">
      <input 
        v-model="formData.mobile_number" 
        type="text" 
        placeholder="Enter your phone number" 
        required 
        autocomplete="off"
    />
    <select v-model="formData.countryCode" required> 
      <option value="" disabled selected>▼</option>
        <option v-for="code in countryCodes" :value="code.value" :key="code.value">{{ code.label }}</option>
    </select>
    </div>
   
    <input v-model="formData.email_address" type="email" placeholder="Email Address" required />
    <input v-model="formData.street_address" placeholder="Street Address" required />
    <input v-model="formData.city_residence" placeholder="City" required />
    <input v-model="formData.state_residence" placeholder="Enter your region/province/state" required />

    <div>
      <br>
      <label>Is your present address the same as your permanent address?</label><br>
      <input type="checkbox" v-model="formData.same_address" />
      <label>Yes</label>
    </div>

    <!-- Always show the permanent address fields -->
    <div class="contact-info">
      <h3>Permanent Address</h3>
      <input v-model="formData.permanent_street_address" :readonly="formData.same_address" placeholder="Street Address" required />
      <input v-model="formData.permanent_city" :readonly="formData.same_address" placeholder="City" required />
      <input v-model="formData.permanent_state" :readonly="formData.same_address" placeholder="Region/Province/State" required />
    </div>
  
  <div class="contact-info-btn">
    <button @click="prevStep">Back</button>
    <button @click="nextStep">Next</button>
  </div>
</div>


        <!-- Step 4: ID Verification -->
        <div v-if="currentStep === 4">
          <h2>Step 4: ID Verification</h2>
          <select v-model="formData.valid_id" required>
  <option value="" disabled selected>Select a Valid ID</option>
  <option value="Passport">Passport</option>
  <option value="Drivers License">Driver's License</option>
  <option value="UMID">Unified Multi-Purpose ID (UMID)</option>
  <option value="National ID">National ID</option>
  <option value="SSS Card">SSS Card</option>
  <option value="GSIS eCard">GSIS eCard</option>
  <option value="PRC ID">PRC ID</option>
  <option value="Voters ID">Voter's ID or Voter's Certificate</option>
  <option value="IBP ID">IBP ID</option>
  <option value="OWWA ID">OWWA ID</option>
  <option value="OFW Card">OFW Card</option>
</select>

          <input v-model="formData.id_no" placeholder="Valid ID No" required />
          <input v-model="formData.id_no" placeholder="Valid until" required />
          <input 
  type="file" 
  accept="image/*" 
  capture="environment" 
  @change="handleFileUpload" 
  required
/>
<input v-model="formData.latest_pic" placeholder="Capture or Upload Your Recent Photo" required />
          <input 
  type="file" 
  accept="image/*" 
  capture="environment" 
  @change="handleFileUpload" 
  required
/>
          <input v-model="formData.work_industry" placeholder="Work Industry" required />
          <input v-model="formData.role" placeholder="Role" required />
          <input v-model="formData.income" type="number" placeholder="Income" required />
          <button @click="prevStep">Back</button>
          <button @click="nextStep">Next</button>
        </div>

        <!-- Step 5: Review & Confirm -->
        <div v-if="currentStep === 5">
          <h2>Step 5: Review & Confirm</h2>
          <div class="review-section">
            <p><strong>Name:</strong> {{ formData.title }} {{ formData.first_name }} {{ formData.last_name }}</p>
            <p><strong>Age:</strong> {{ formData.age }}</p>
            <p><strong>Citizenship:</strong> {{ formData.citizenship }}</p>
            <p><strong>Mobile:</strong> {{ formData.mobile_number }}</p>
            <p><strong>Email:</strong> {{ formData.email_address }}</p>
            <p><strong>Address:</strong> {{ formData.street_address }}, {{ formData.city_residence }}, {{ formData.state_residence }}</p>
            <p><strong>Valid ID:</strong> {{ formData.valid_id }}</p>
            <p><strong>ID No:</strong> {{ formData.id_no }}</p>
            <p><strong>Industry:</strong> {{ formData.work_industry }}</p>
            <p><strong>Role:</strong> {{ formData.role }}</p>
            <p><strong>Income:</strong> {{ formData.income }}</p>
          </div>
          <button @click="prevStep">Back</button>
          <button type="submit">Submit</button>
        </div>

      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  
  data() {
    return {
      currentStep: 1, // Track the current step
      showErrors: false, // Flag to show validation errors
      formData: {
        title: "",
        last_name: "",
        first_name: "",
        age: "",
        citizenship: "",
        countryCode: '',  
        mobile_number: '',
        email_address: "",
        present_address: false,
        street_address: "",
        city_residence: "",
        state_residence: "",
        same_address: false,
        permanent_street_address: "",
        permanent_city: "",
        permanent_state: "",
        valid_id: "",
        id_no: "",
        photo_id: "",
        work_industry: "",
        role: "",
        income: "",
        agreeToPrivacy: false,
        isOver21: false,
        nationality: "",
      },
      isOpen: false,
      nationality: "",
      selectedNationality: "",
      nationalities: [
  { name: 'Afghan' },
  { name: 'Albanian' },
  { name: 'Algerian' },
  { name: 'American' },
  { name: 'Andorran' },
  { name: 'Angolan' },
  { name: 'Antiguan' },
  { name: 'Argentine' },
  { name: 'Armenian' },
  { name: 'Australian' },
  { name: 'Austrian' },
  { name: 'Azerbaijani' },
  { name: 'Bahaman' },
  { name: 'Bahraini' },
  { name: 'Bangladeshi' },
  { name: 'Barbadian' },
  { name: 'Belgian' },
  { name: 'Belizean' },
  { name: 'Beninese' },
  { name: 'Bhutanese' },
  { name: 'Bolivian' },
  { name: 'Bosnian' },
  { name: 'Botswanan' },
  { name: 'Brazilian' },
  { name: 'British' },
  { name: 'Bruneian' },
  { name: 'Bulgarian' },
  { name: 'Burkinabe' },
  { name: 'Burundian' },
  { name: 'Cambodian' },
  { name: 'Cameroonian' },
  { name: 'Canadian' },
  { name: 'Cape Verdean' },
  { name: 'Central African' },
  { name: 'Chadian' },
  { name: 'Chilean' },
  { name: 'Chinese' },
  { name: 'Colombian' },
  { name: 'Comorian' },
  { name: 'Congolese' },
  { name: 'Costa Rican' },
  { name: 'Croatian' },
  { name: 'Cuban' },
  { name: 'Cypriot' },
  { name: 'Czech' },
  { name: 'Danish' },
  { name: 'Djiboutian' },
  { name: 'Dominican' },
  { name: 'Dominican Republic' },
  { name: 'Egyptian' },
  { name: 'Emirati' },
  { name: 'Equatorial Guinean' },
  { name: 'Eritrean' },
  { name: 'Estonian' },
  { name: 'Ethiopian' },
  { name: 'Fijian' },
  { name: 'Filipino' },
  { name: 'Finnish' },
  { name: 'French' },
  { name: 'Gabonese' },
  { name: 'Gambian' },
  { name: 'Georgian' },
  { name: 'German' },
  { name: 'Ghanaian' },
  { name: 'Greece' },
  { name: 'Grenadian' },
  { name: 'Guatemalan' },
  { name: 'Guinean' },
  { name: 'Guyanese' },
  { name: 'Haitian' },
  { name: 'Honduran' },
  { name: 'Hungarian' },
  { name: 'Icelander' },
  { name: 'Indian' },
  { name: 'Indonesian' },
  { name: 'Iranian' },
  { name: 'Iraqi' },
  { name: 'Irish' },
  { name: 'Israeli' },
  { name: 'Italian' },
  { name: 'Jamaican' },
  { name: 'Japanese' },
  { name: 'Jordanian' },
  { name: 'Kazakhstani' },
  { name: 'Kenyan' },
  { name: 'Kittian and Nevisian' },
  { name: 'Korean' },
  { name: 'Kuwaiti' },
  { name: 'Kyrgyzstani' },
  { name: 'Laotian' },
  { name: 'Latvian' },
  { name: 'Lebanese' },
  { name: 'Lesotho' },
  { name: 'Liberian' },
  { name: 'Libyan' },
  { name: 'Liechtenstein' },
  { name: 'Lithuanian' },
  { name: 'Luxembourgish' },
  { name: 'Macedonian' },
  { name: 'Malagasy' },
  { name: 'Malawian' },
  { name: 'Malaysian' },
  { name: 'Maldivian' },
  { name: 'Malian' },
  { name: 'Malta' },
  { name: 'Marshallese' },
  { name: 'Mauritian' },
  { name: 'Mauritanian' },
  { name: 'Mexican' },
  { name: 'Micronesian' },
  { name: 'Moldovan' },
  { name: 'Monacan' },
  { name: 'Mongolian' },
  { name: 'Moroccan' },
  { name: 'Mozambican' },
  { name: 'Namibian' },
  { name: 'Nauruan' },
  { name: 'Nepalese' },
  { name: 'New Zealand' },
  { name: 'Nicaraguan' },
  { name: 'Nigerian' },
  { name: 'Nigerien' },
  { name: 'Norwegian' },
  { name: 'Omani' },
  { name: 'Pakistani' },
  { name: 'Palauan' },
  { name: 'Panamanian' },
  { name: 'Papua New Guinean' },
  { name: 'Paraguayan' },
  { name: 'Peruvian' },
  { name: 'Polish' },
  { name: 'Portuguese' },
  { name: 'Qatari' },
  { name: 'Romanian' },
  { name: 'Russian' },
  { name: 'Rwandan' },
  { name: 'Saint Kitts and Nevisian' },
  { name: 'Saint Lucian' },
  { name: 'Saint Vincentian' },
  { name: 'Salvadoran' },
  { name: 'Samoan' },
  { name: 'San Marino' },
  { name: 'Sao Tomean' },
  { name: 'Saudi' },
  { name: 'Senegalese' },
  { name: 'Serbian' },
  { name: 'Seychellois' },
  { name: 'Sierra Leonean' },
  { name: 'Singaporean' },
  { name: 'Slovak' },
  { name: 'Slovenian' },
  { name: 'Solomon Islands' },
  { name: 'Somali' },
  { name: 'South African' },
  { name: 'South Korean' },
  { name: 'Spanish' },
  { name: 'Sri Lankan' },
  { name: 'Sudanese' },
  { name: 'Surinamese' },
  { name: 'Swazi' },
  { name: 'Swedish' },
  { name: 'Swiss' },
  { name: 'Syrian' },
  { name: 'Taiwanese' },
  { name: 'Tajikistani' },
  { name: 'Tanzanian' },
  { name: 'Thai' },
  { name: 'Togolese' },
  { name: 'Tongan' },
  { name: 'Trinidadian and Tobagonian' },
  { name: 'Tunisian' },
  { name: 'Turkish' },
  { name: 'Turkmenistani' },
  { name: 'Tuvaluan' },
  { name: 'Ugandan' },
  { name: 'Ukrainian' },
  { name: 'Uruguayan' },
  { name: 'Uzbekistani' },
  { name: 'Venezuelan' },
  { name: 'Vietnamese' },
  { name: 'Yemeni' },
  { name: 'Zambian' },
  { name: 'Zimbabwean' },
],
filteredNationalities: [],
countryCodes: [
            { value: '+1', label: '+1 (United States, Canada, Mexico, etc.)' },
            { value: '+44', label: '+44 (United Kingdom)' },
            { value: '+91', label: '+91 (India)' },
            { value: '+61', label: '+61 (Australia)' },
            { value: '+81', label: '+81 (Japan)' },
            { value: '+33', label: '+33 (France)' },
            { value: '+49', label: '+49 (Germany)' },
            { value: '+34', label: '+34 (Spain)' },
            { value: '+39', label: '+39 (Italy)' },
            { value: '+55', label: '+55 (Brazil)' },
            { value: '+27', label: '+27 (South Africa)' },
            { value: '+86', label: '+86 (China)' },
            { value: '+7', label: '+7 (Russia, Kazakhstan)' },
            { value: '+52', label: '+52 (Mexico)' },
            { value: '+64', label: '+64 (New Zealand)' },
            { value: '+966', label: '+966 (Saudi Arabia)' },
            { value: '+82', label: '+82 (South Korea)' },
            { value: '+20', label: '+20 (Egypt)' },
            { value: '+41', label: '+41 (Switzerland)' },
            { value: '+31', label: '+31 (Netherlands)' },
            { value: '+46', label: '+46 (Sweden)' },
            { value: '+48', label: '+48 (Poland)' },
            { value: '+32', label: '+32 (Belgium)' },
            { value: '+353', label: '+353 (Ireland)' },
            { value: '+62', label: '+62 (Indonesia)' },
            { value: '+54', label: '+54 (Argentina)' },
            { value: '+56', label: '+56 (Chile)' },
            { value: '+64', label: '+64 (New Zealand)' },
            { value: '+380', label: '+380 (Ukraine)' },
            { value: '+92', label: '+92 (Pakistan)' },
            { value: '+63', label: '+63 (Philippines)' },
            { value: '+977', label: '+977 (Nepal)' },
            { value: '+98', label: '+98 (Iran)' },
            { value: '+963', label: '+963 (Syria)' },
            { value: '+254', label: '+254 (Kenya)' },
            { value: '+855', label: '+855 (Cambodia)' },
            { value: '+234', label: '+234 (Nigeria)' },
            { value: '+254', label: '+254 (Kenya)' },
            { value: '+359', label: '+359 (Bulgaria)' },
            { value: '+375', label: '+375 (Belarus)' },
            { value: '+354', label: '+354 (Iceland)' },
            { value: '+977', label: '+977 (Nepal)' },
            { value: '+995', label: '+995 (Georgia)' },
            { value: '+974', label: '+974 (Qatar)' },
            { value: '+850', label: '+850 (North Korea)' },
            { value: '+966', label: '+966 (Saudi Arabia)' },
            { value: '+1', label: '+1 (United States, Canada, Mexico, etc.)' },
            { value: '+82', label: '+82 (South Korea)' },
            { value: '+212', label: '+212 (Morocco)' },
            { value: '+971', label: '+971 (United Arab Emirates)' },
            { value: '+60', label: '+60 (Malaysia)' },
            { value: '+91', label: '+91 (India)' },
            { value: '+93', label: '+93 (Afghanistan)' },
            { value: '+973', label: '+973 (Bahrain)' },
            { value: '+1242', label: '+1242 (Bahamas)' },
            { value: '+267', label: '+267 (Botswana)' },
            { value: '+855', label: '+855 (Cambodia)' },
            { value: '+226', label: '+226 (Burkina Faso)' },
            { value: '+228', label: '+228 (Togo)' },
            { value: '+234', label: '+234 (Nigeria)' },
            { value: '+261', label: '+261 (Madagascar)' },
            { value: '+685', label: '+685 (Samoa)' },
            { value: '+255', label: '+255 (Tanzania)' },
            { value: '+678', label: '+678 (Vanuatu)' },
            { value: '+1849', label: '+1849 (Dominican Republic)' },
            { value: '+1868', label: '+1868 (Trinidad and Tobago)' },
            { value: '+1880', label: '+1880 (Barbados)' },
            { value: '+1', label: '+1 (USA, Canada, Mexico, etc.)' },
            { value: '+44', label: '+44 (United Kingdom)' },
            { value: '+971', label: '+971 (UAE)' },
            { value: '+54', label: '+54 (Argentina)' },
            { value: '+62', label: '+62 (Indonesia)' },
            { value: '+93', label: '+93 (Afghanistan)' },
            { value: '+54', label: '+54 (Argentina)' },
            { value: '+96', label: '+96 (Seychelles)' },
            { value: '+81', label: '+81 (Japan)' },
            { value: '+222', label: '+222 (Mauritania)' },
            { value: '+43', label: '+43 (Austria)' },
            { value: '+501', label: '+501 (Belize)' },
            { value: '+506', label: '+506 (Costa Rica)' },
            { value: '+503', label: '+503 (El Salvador)' },
            { value: '+504', label: '+504 (Honduras)' },
            { value: '+505', label: '+505 (Nicaragua)' },
            { value: '+507', label: '+507 (Panama)' },
            { value: '+508', label: '+508 (Saint Pierre and Miquelon)' },
            { value: '+509', label: '+509 (Haiti)' },
            { value: '+591', label: '+591 (Bolivia)' },
            { value: '+593', label: '+593 (Ecuador)' },
            { value: '+594', label: '+594 (French Guiana)' },
            { value: '+595', label: '+595 (Paraguay)' },
            { value: '+596', label: '+596 (Martinique)' },
            { value: '+597', label: '+597 (Suriname)' },
            { value: '+598', label: '+598 (Uruguay)' },
            { value: '+599', label: '+599 (Curaçao)' },
            { value: '+20', label: '+20 (Egypt)' },
            { value: '+33', label: '+33 (France)' },
            { value: '+40', label: '+40 (Romania)' },
            { value: '+41', label: '+41 (Switzerland)' },
            { value: '+47', label: '+47 (Norway)' },
            { value: '+48', label: '+48 (Poland)' },
            { value: '+49', label: '+49 (Germany)' },
            { value: '+51', label: '+51 (Peru)' },
            { value: '+52', label: '+52 (Mexico)' },
            { value: '+53', label: '+53 (Cuba)' },
            { value: '+54', label: '+54 (Argentina)' },
            { value: '+55', label: '+55 (Brazil)' },
            { value: '+56', label: '+56 (Chile)' },
            { value: '+57', label: '+57 (Colombia)' },
            { value: '+58', label: '+58 (Venezuela)' },
            { value: '+59', label: '+59 (Dutch Caribbean)' },
            { value: '+60', label: '+60 (Malaysia)' },
            { value: '+61', label: '+61 (Australia)' },
            { value: '+62', label: '+62 (Indonesia)' },
            { value: '+63', label: '+63 (Philippines)' },
            { value: '+64', label: '+64 (New Zealand)' },
            { value: '+65', label: '+65 (Singapore)' },
            { value: '+66', label: '+66 (Thailand)' },
            { value: '+67', label: '+67 (Western Australia)' },
            { value: '+68', label: '+68 (Timor Leste)' },
            { value: '+69', label: '+69 (Indian Ocean Territories)' },
            { value: '+70', label: '+70 (Romania)' },
            { value: '+71', label: '+71 (Norway)' },
            { value: '+72', label: '+72 (Fiji)' },
            { value: '+73', label: '+73 (Seychelles)' },
            { value: '+74', label: '+74 (Turkmenistan)' },
            { value: '+75', label: '+75 (Uzbekistan)' },
            { value: '+678', label: '+678 (Vanuatu)' },
            { value: '+379', label: '+379 (Vatican City)'},
            { value: '+58', label: '+58 (Venezuela)'},
            { value: '+84', label: '+84 (Vietnam)'},
            { value: '+1', label: '+1 (Virgin Islands)'},
            { value: '+681', label: '+681 (Wallis and Futuna)'},
            { value: '+967', label: '+967 (Yemen)'},
            { value: '+260', label: '+260 (Zambia)'},
            { value: '+263', label: '+263 (Zimbabwe)'},
        ]
    };
  },
  methods: {
    nextStep() {
      if (this.validateStep()) {
        this.currentStep++;
      }
    },
    prevStep() {
      this.currentStep--;
    },

    toggleDropdown() {
      this.isOpen = !this.isOpen;

    },

    selectNationality(name) {
      this.selectedNationality = name;
      this.formData.nationality = name;  // Set selected nationality to form data
      this.isOpen = false;  // Close dropdown
    },

    validateStep() {
  this.showErrors = true; // Enable error messages

  switch (this.currentStep) {
    case 1:
      if (!this.formData.agreeToPrivacy || !this.formData.isOver21) {
        alert("You must agree to the privacy statement and Terms & Conditions.");
        return false;
      }
      break;

    case 2:
      if (!this.formData.first_name || !this.formData.last_name) {
        alert("Please enter your first and last name.");
        return false;
      }
      if (!this.formData.age || this.formData.age < 21) {
        alert("You must be 21 or older.");
        return false;
      }
      break;

    case 3:
      if (!this.formData.email_address) {
        alert("Please enter your email address.");
        return false;
      }
      if (!this.formData.mobile_number) {
        alert("Please enter your mobile number.");
        return false;
      }
      if (!this.formData.street_address) {
        alert("Please enter your present address.");
        return false;
      }
      if (!this.formData.city_residence) {
        alert("Please enter your city residence");
        return false;
      }
      if (!this.formData.state_residence) {
        alert("Please enter your state residence.");
        return false;
      }

      // Validate permanent address only if the 'sameAddress' checkbox is unchecked
      if (!this.sameAddress) {
        if (!this.formData.permanent_street_address) {
          alert("Please enter your permanent street address.");
          return false;
        }
        if (!this.formData.permanent_city) {
          alert("Please enter your permanent city.");
          return false;
        }
        if (!this.formData.permanent_state) {
          alert("Please enter your permanent state.");
          return false;
        }
      }
      break;

    case 4:
      if (!this.formData.valid_id) {
        alert("Please enter a valid ID.");
        return false;
      }
      if (!this.formData.id_no) {
        alert("Please enter your ID number.");
        return false;
      }
      break;

    default:
      return true;
  }

  return true; // Allow moving to the next step if all validations pass

    },
    async submitForm() {
      try {
        await axios.post("http://192.168.1.11:8000/api/form-records/", this.formData);
        alert("Form submitted successfully!");
        this.resetForm();
      } catch (error) {
        console.error("Error submitting form:", error);
        alert("An error occurred while submitting.");
      }
    },
    resetForm() {
      this.currentStep = 1;
      this.showErrors = false;
    },
    filterNationalities() {
      this.filteredNationalities = this.nationalities.filter((nationality) =>
      nationality.name.toLowerCase().includes(this.formData.nationality.toLowerCase())
      );
    }
  },
  computed: {
    filteredNationalities() {
      return this.nationalities.filter((item) =>
        item.name.toLowerCase().includes(this.formData.nationality.toLowerCase())
      );
    },
  },
  mounted() {
    this.filteredNationalities = this.nationalities; // Load all initially
  },
  watch: {
    "formData.same_address"(newValue) {
      if (newValue) {
        // Autofill the permanent address when the checkbox is checked
        this.formData.permanent_street_address = this.formData.street_address;
        this.formData.permanent_city = this.formData.city_residence;
        this.formData.permanent_state = this.formData.state_residence;
      }
    },
    "formData.street_address"(newValue) {
      if (this.formData.same_address) this.formData.permanent_street_address = newValue;
    },
    "formData.city_residence"(newValue) {
      if (this.formData.same_address) this.formData.permanent_city = newValue;
    },
    "formData.state_residence"(newValue) {
      if (this.formData.same_address) this.formData.permanent_state = newValue;
    }
  }
};
</script>


<style scoped>
.onyx-header h1{
  font-weight: bold;
}
.onyx-header p{
  color: grey;
}
.onyx-header li{
  list-style: none;
  margin-top: 1rem;
}
strong{
  color: red;
}

.form-container{
  max-width: 1000px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
  background-color: #ffffff;
  color: rgb(0, 0, 0);
  border: 1px solid #b0afaf7c;
  border-radius: 3px;
  margin-top: 5rem;
}
.form-consents{
  width: 100%;
  margin-bottom: 1rem;
}

button{
  padding: 0.5rem 1rem;
  border: none;
  background-color: #ffeb13;
}

button:hover{
  background-color: #ffb013;
}
.country-code-wrapper {
  position: relative;
    width: 350px;
    display: flex;
    align-items: center;
   
    border-radius: 5px;
    overflow: hidden;
    background: white;
}

.country-code-wrapper input {
  flex: 1;
    padding: 10px;
    padding-right: 60px; /* Space for the select dropdown */
    border: none;
    outline: none;
    font-size: 16px;
    border: 1px solid grey;
}

.country-code-wrapper select {
  position: absolute;
    right: 2.5rem;
    top: 1.5rem;
    height: 20px;
    width: 50px;
    border: none;
    padding: 0 10px;
    font-size: 16px;
    cursor: pointer;
    outline: none;
    appearance: none;
    
}
.form-consents p{
  font-weight: bold;
}
.form-consents a{
  text-decoration: none;
  color: #13c0ff;
}

.form-consents input{
  margin-top: 1rem;
}

.form-consents span{
  color: rgba(255, 101, 19, 0.897);
}
.form-row{
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.form-row input{
  padding: 1rem;
  width: 100%;
}

.form-row select{
  width: 100%;
  padding: 1rem;
}
.form-box{
  display: flex;
}
.red-dot{
  color: red;
}
.red-dot label{
  color: black;
}

.progress-bar {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.progress-bar div {
  width: 30px;
  height: 30px;
  background: lightgray;
  border-radius: 50%;
  margin: 0 5px;
  text-align: center;
  line-height: 30px;
}

.progress-bar .active {
  background: green;
  color: white;
}

/* Personal Information styling */
.personal-info{
  display: flex;
  flex-direction: column;
  width: 60vw;
  max-width: 900px;
}
.personal-info select{
  padding: 0.5rem;
  max-width: 320px;
}
.personal-info input{
  padding: 0.5rem;
  margin-top: 1rem;
  max-width: 300px;
}
.personal-info-btn {
  display: flex;
  flex-direction: row;
  gap: 1rem;
  margin-top: 1rem;
}
.dropdown {
  position: relative;
  width: 200px;
}
.dropdown input {
  width: 30vw;
  max-width: 300px;
  padding: 0.5rem;
  border: 1px solid grey;
  border-radius: 3px;
}
.dropdown-menu {
  position: absolute;
  width: 100%;
  max-height: 200px;
  overflow-y: auto;
  background: white;
  border: 1px solid #ccc;
  border-radius: 4px;
  list-style: none;
  padding: 0;
  margin: 0;
}
.dropdown-menu li {
  padding: 8px;
  cursor: pointer;
}
.dropdown-menu li:hover {
  background: #f0f0f0;
}
/* Contact Information styling */
.contact-info{
  display: flex;
  flex-direction: column;
  width: 60vw;
  max-width: 900px;
}
.contact-info input{
  padding: 0.5rem;
  margin-top: 1rem;
  max-width: 300px;
}
.contact-info-btn {
  display: flex;
  flex-direction: row;
  gap: 1rem;
  margin-top: 1rem;
}

</style>