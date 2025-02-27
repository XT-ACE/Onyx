<template>
  <div class="onyx-form">
    <div class="form-container">
      <div class="onyx-banner">
      <img src="/images/onyxheader.jpg" class="banner">
      </div>
      <div class="form-group">
      <div class="onyx-header">
        <h1>CF - ONYX MEMBERSHIP CARD APPLICATION FORM</h1>
  <p>
    The following personalities are NOT ALLOWED to register and/or play in this casino:
  </p>
  
  <button @click="toggleList">{{ listVisible ? 'Hide List' : 'Show List' }}</button>
  
  <ul v-if="listVisible">
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
              <label><span style="color: red;">*</span>
                I agree to the 
                <a href="https://www.pagcor.ph/docs/data-privacy-notice.pdf" target="_blank">
                  Privacy Statement
                </a>
              </label><br>
              <span v-if="!formData.agreeToPrivacy && showErrors" class="error-message">
                This is a required field!
              </span>
            </div>
            <div>
              <input v-model="formData.isOver21" type="checkbox" />
              <label><span style="color: red;">*</span> I agree to the <a href="https://www.pagcor.ph/regulatory/pdf/RG-Code-of-Practice-v6.pdf" target="_blank">
                  Terms and Conditions
                </a></label><br>
              <span v-if="!formData.isOver21 && showErrors" class="error-message">
                This is a required field!
              </span>
            </div>
          </div>
          <button @click="nextStep">Next</button>
          <p>Powered by: ACE Systems</p>
        </div>

        <!-- Step 2: Personal Information -->
        <div class="input-info" v-if="currentStep === 2">
          <h2>Step 2: Personal Information</h2>
          <label><span style="color: red;">*</span> Title:</label>
          <select v-model="formData.title" required>
            <option value="" disabled>Title</option>
            <option value="Mr.">Mr.</option>
            <option value="Mrs.">Mrs.</option>
            <option value="Ms.">Ms.</option>
          </select>
          <label><span style="color: red;">*</span> Last Name:</label>
          <input v-model="formData.last_name" placeholder="Enter your last name" required />
          <label><span style="color: red;">*</span> First Name:</label>
          <input v-model="formData.first_name" placeholder="Enter your first name" required />
           <!-- Date of Birth Input -->
           <label><span style="color: red;">*</span> Birth Date:</label>
    <input 
      type="date" 
      v-model="formData.date_of_birth" 
      @input="calculateAge"
      required 
      class="date"
    />
    <label><span style="color: red;">*</span> Place of Birth:</label>
          <input v-model="formData.place_of_birth" placeholder="Place of Birth" required />
          <label>Gender:</label>
          <select v-model="formData.gender" required>
            <option value="" disabled>Gender</option>
            <option value="Male">Male</option>
            <option value="Female">Female</option>
          </select>
            <!-- Age Input (Auto-Computed) -->
            <label><span style="color: red;">*</span> Age:</label>
    <input 
      v-model="formData.age" 
      type="number" 
      placeholder="Age" 
      required 
      readonly
    />

    <!-- Age Restriction Warning -->
    <span v-if="formData.age && formData.age < 21" class="error-message">
      You must be 21 or older
    </span>
          <div class="dropdown" ref="dropdown">

            <label><span style="color: red;">*</span> Nationality:</label>
    <input
      type="text"
      v-model="formData.nationality"
      placeholder="Search Nationality"
      @focus="isOpen = true"
      @input="filterNationalities"
      required
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
  <div class="input-info-btn">
    <button @click="prevStep">Back</button>
    <button @click="nextStep">Next</button>
  </div>
  </div>
        <!-- Step 3: Contact Information -->
        <div class="input-info" v-if="currentStep === 3">
    <h2>Step 3: Contact Information</h2>
<label><span style="color: red;">*</span> Phone Number:</label>
    <vue-tel-input
      v-model="formData.mobile_number"
      :preferred-countries="['us', 'gb', 'ph']"
      placeholder="Enter your phone number"
      required
      autocomplete="off"
      ref="phoneInput"
      mode="international"
      class="phone-number"
    />
    <label><span style="color: red;">*</span> Email:</label>
    <input v-model="formData.email_address" type="email" placeholder="Email Address" required />
    <label><span style="color: red;">*</span> Street Address:</label>
    <input v-model="formData.street_address" placeholder="Street Address" required />
    <label><span style="color: red;">*</span> City:</label>
    <input v-model="formData.city_residence" placeholder="City" required />
    <label><span style="color: red;">*</span> Region | Province | State:</label>
    <input v-model="formData.state_residence" placeholder="Enter your region/province/state" required />

    <div>
      <br>
      <label>Is your present address the same as your permanent address?</label><br>
      <label class="label-box"><input class="checkbox" type="checkbox" v-model="formData.same_address" />
      Yes</label>
    </div>

    <!-- Always show the permanent address fields -->
    
      <h3>Permanent Address</h3>
      <label><span style="color: red;">*</span> Street Address:</label>
      <input v-model="formData.permanent_street_address" :readonly="formData.same_address" placeholder="Street Address" required />
      <label><span style="color: red;">*</span> City:</label>
      <input v-model="formData.permanent_city" :readonly="formData.same_address" placeholder="City" required />
      <label><span style="color: red;">*</span> Region | Province | State:</label>
      <input v-model="formData.permanent_state" :readonly="formData.same_address" placeholder="Region/Province/State" required />
    
  
  <div class="input-info-btn">
    <button @click="prevStep">Back</button>
    <button @click="nextStep">Next</button>
  </div>
</div>


        <!-- Step 4: ID Verification -->
        <div class="input-info" v-if="currentStep === 4">
          <h2>Step 4: ID Verification</h2>

          <label><span style="color: red;">*</span> Valid ID:</label>
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
         <label><span style="color: red;">*</span> ID No:</label>
          <input v-model="formData.id_no" placeholder="Valid ID No" required />
          <label><span style="color: red;">*</span> Valid Until:</label>
          <input
  v-model="formData.valid_until"
  type="date"
  placeholder="Valid until"
  required
  :min="minDate"
  class="date"
/>
<p v-if="errorMessage" style="color: red;">{{ errorMessage }}</p>

<div class="upload-container">
    <!-- Front ID Upload -->
    <label class="custom-upload">
      <span>{{ frontFileName || "📷 Upload Front ID" }}</span>
      <input 
        type="file" 
        accept="image/*" 
        @change="handleFileUploadFrontID"
        required
      />
    </label>
    <img v-if="frontIDPreview" :src="frontIDPreview" alt="Front ID Preview" class="preview-image" />

    <!-- Back ID Upload -->
    <label class="custom-upload">
      <span>{{ backFileName || "📷 Upload Back ID" }}</span>
      <input 
        type="file" 
        accept="image/*" 
        @change="handleFileUploadBackID"
        required
      />
    </label>
    <img v-if="backIDPreview" :src="backIDPreview" alt="Back ID Preview" class="preview-image" />
  </div>
<label><span style="color: red;">*</span> Work Industry:</label>
<select v-model="formData.work_industry" @change="checkOtherIndustry" required>
  <option value="" disabled>Select Work Industry</option>
<option value="Accountancy">Accountancy</option>
<option value="Advertising">Advertising</option>
<option value="Agriculture">Agriculture</option>
<option value="Architecture">Architecture</option>
<option value="Automotive">Automotive</option>
<option value="Banking">Banking</option>
<option value="Construction">Construction</option>
<option value="Customer Service">Customer Service</option>
<option value="Education">Education</option>
<option value="Engineering">Engineering</option>
<option value="Entertainment">Entertainment</option>
<option value="Finance">Finance</option>
<option value="Food & Beverage">Food & Beverage</option>
<option value="Government">Government</option>
<option value="Healthcare">Healthcare</option>
<option value="Hospitality">Hospitality</option>
<option value="Human Resources">Human Resources</option>
<option value="IT">IT</option>
<option value="Legal">Legal</option>
<option value="Logistics">Logistics</option>
<option value="Manufacturing">Manufacturing</option>
<option value="Marketing">Marketing</option>
<option value="Media">Media</option>
<option value="Non-Profit">Non-Profit</option>
<option value="Pharmaceutical">Pharmaceutical</option>
<option value="Real Estate">Real Estate</option>
<option value="Retail">Retail</option>
<option value="Sales">Sales</option>
<option value="Telecommunications">Telecommunications</option>
<option value="Tourism">Tourism</option>
<option value="Transportation">Transportation</option>
<option value="Others">Others</option>
</select>

<input 
class="others"
  v-if="showOtherInput" 
  v-model="formData.work_industry" 
  placeholder="Please specify" 
  required 
/>
          <label><span style="color: red;">*</span> Role:</label>
          <input v-model="formData.role" placeholder="Role" required />
          <label><span style="color: red;">*</span> Income:</label>
          <input v-model="formData.income" type="number" placeholder="Income" required />
          <div class="input-info-btn">
         <button @click="prevStep">Back</button>
         <button @click="nextStep">Next</button>
  </div>
        </div>

        <!-- Step 5: Review & Confirm -->
        <div v-if="currentStep === 5">
          <h2>Step 5: Review & Confirm</h2>
          <h3>Consent and Acknowledgment</h3>


          <div class="consent-acknowledgement">
    <!-- Checkbox for Marketing Consent -->
    <label>
      <input type="checkbox" v-model="formData.marketing_consent" /><span style="color: red;">*</span>
      I agree to receive promotional offers, advertisements, and marketing communications from CF-ONYX CASINO through email, social media, and/or SMS.
    </label>
<br><br>
    <!-- Checkbox for Data Privacy Agreement -->
    <label>
      <input type="checkbox" v-model="formData.privacy_consent" required /><span style="color: red;">*</span>
      I have read and understood this form, including the Privacy Notice, and consent to the processing of my personal data. I acknowledge that I am fully aware of my rights under the Data Privacy Act of 2012 and understand that my consent does not preclude the existence of other lawful grounds for processing my personal data.
    </label>
  </div>
          <div class="review-section">
            <p><strong>Name:</strong> {{ formData.title }} {{ formData.first_name }} {{ formData.last_name }}</p>
            <p><strong>Age:</strong> {{ formData.age }}</p>
            <p><strong>Gender:</strong> {{ formData.gender }}</p>
            <p><strong>Birth Date:</strong> {{ formData.date_of_birth }}</p>
            <p><strong>Address:</strong> {{ formData.place_of_birth }}</p>
            <p><strong>Mobile:</strong> {{ formData.mobile_number }}</p>
            <p><strong>Email:</strong> {{ formData.email_address }}</p>
            <p><strong>Address:</strong> {{ formData.street_address }}, {{ formData.city_residence }}, {{ formData.state_residence }}</p>
            <p><strong>Valid ID:</strong> {{ formData.valid_id }}</p>
            <p><strong>ID No:</strong> {{ formData.id_no }}</p>
            <p><strong>Front ID:</strong><img v-if="frontIDPreview" :src="frontIDPreview" alt="Front ID Preview" style="max-width: 200px; display: block; margin-top: 10px;" /></p>
            <p><strong>Back ID:</strong><img v-if="backIDPreview" :src="backIDPreview" alt="Back ID Preview" style="max-width: 200px; display: block; margin-top: 10px;" /></p>
            <p><strong>Industry:</strong> {{ formData.work_industry }}</p>
            <p><strong>Role:</strong> {{ formData.role }}</p>
            <p><strong>Income:</strong> {{ formData.income }}</p>
          </div>
     
    <!-- E-Signature Input -->
    <div class="signature-container">
      <p>E-Signature (Draw below)</p>
      <VueSignaturePad ref="signaturePad" class="signature-pad" /><br>
      <button type="button" @click="clearSignature">Clear</button>
    </div>
    <div class="submit">
          <button @click="prevStep">Back</button>
          <button type="submit">Submit</button>
        </div>
        </div>
 <!-- Success Modal -->
 <div v-if="showSuccessModal" class="modal-overlay">
      <div class="modal">
        <h3>Form Submitted Successfully!</h3>
        <p>Your form has been submitted successfully.</p>
        <button @click="closeModal">OK</button>
      </div>
    </div>
      </form>
    </div>
  </div>
  </div>
</template>

<script>
import axios from "axios";
import { ref } from "vue";
  import { VueTelInput } from "vue-tel-input";
  import "vue-tel-input/vue-tel-input.css";
  import { VueSignaturePad } from "vue-signature-pad";
  
export default {
  components: {
    VueTelInput,
    VueSignaturePad,
  },
  data() {
    return {
      listVisible: false,
      currentStep: 1, // Track the current step
      showErrors: false, // Flag to show validation errors
      showSuccessModal: false, // Controls modal visibility
      formData: {
        title: "",
        last_name: "",
        first_name: "",
        age: "",
        date_of_birth: '',
        place_of_birth: '',
        gender: '',
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
        valid_until: '',
        id_front: null,
        id_back: null,
        work_industry: "",
        role: "",
        income: "",
        agreeToPrivacy: false,
        isOver21: false,
        nationality: "",
        signature: "",
        marketing_consent: false, // Optional checkbox
        privacy_consent: false,   // Required checkbox
        id: "",
      },
      selectedIndustry: "", // This will hold the industry value
      showOtherInput: false,
      frontFileName: "",
      backFileName: "",
      frontIDPreview: null,
      backIDPreview: null,
      errorMessage: '',
      minDate: new Date().toISOString().split('T')[0], // Get today's date in YYYY-MM-DD format
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
    };
  },
  methods: {
    nextStep() {
  if (this.validateStep()) {
    this.currentStep++;
    window.scrollTo(0, 0); // Scroll to the top
  }
},
prevStep() {
  this.currentStep--;
  window.scrollTo(0, 0); // Scroll to the top
 },
    toggleList() {
      this.listVisible = !this.listVisible; // Toggle the visibility state
    },
    toggleDropdown() {
      this.isOpen = !this.isOpen;

    },
    clearSignature() {
      this.$refs.signaturePad.clearSignature();
    },
    selectNationality(name) {
      this.selectedNationality = name;
      this.formData.nationality = name;  // Set selected nationality to form data
      this.isOpen = false;  // Close dropdown
    },
    handleFileUploadFrontID(event) {
      const file = event.target.files[0];
      if (file) {
        this.formData.id_front = file;
        this.frontIDPreview = URL.createObjectURL(file);
        this.frontFileName = `📄 ${file.name}`; // Display the file name
      }
    },
    handleFileUploadBackID(event) {
      const file = event.target.files[0];
      if (file) {
        this.formData.id_back = file;
        this.backIDPreview = URL.createObjectURL(file);
        this.backFileName = `📄 ${file.name}`; // Display the file name
      }
    },
    checkOtherIndustry() {
  if (this.formData.work_industry === "Others") {
    this.showOtherInput = true;
    this.formData.work_industry = ""; // Clear value for manual entry
  } else {
    this.showOtherInput = false;
  }
}
,
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
        const signatureData = this.$refs.signaturePad.saveSignature();
        if (!signatureData || !signatureData.data) {
          console.error("Signature data is missing:", signatureData);
          alert("Signature is missing. Please sign before submitting.");
          return;
        }

        const base64Image = signatureData.data;
        if (typeof base64Image !== "string" || !base64Image.includes(",")) {
          console.error("Invalid base64 image format:", base64Image);
          alert("Error: Signature is not in the correct format.");
          return;
        }

        const blob = this.dataURLtoBlob(base64Image);

        const formData = new FormData();
        formData.append("privacy_consent", this.formData.privacy_consent);
        formData.append("signature", blob, "signature.png");

        for (const key in this.formData) {
          if (key !== "signature") {
            formData.append(key, this.formData[key]);
          }
        }

        const response = await axios.post("http://192.168.1.11:8000/api/form-records/", formData, {
          headers: { "Content-Type": "multipart/form-data" },
        });

        const id = response.data.id;

        // Show success modal instead of alert
        this.showSuccessModal = true;

        // Redirect after closing the modal
        this.redirectId = id;

      } catch (error) {
        console.error("Error submitting form:", error);
        alert("An error occurred while submitting.");
      }
    },

    dataURLtoBlob(dataURL) {
      try {
        const byteString = atob(dataURL.split(",")[1]);
        const mimeString = dataURL.split(",")[0].split(":")[1].split(";")[0];

        const ab = new ArrayBuffer(byteString.length);
        const ia = new Uint8Array(ab);
        for (let i = 0; i < byteString.length; i++) {
          ia[i] = byteString.charCodeAt(i);
        }

        return new Blob([ab], { type: mimeString });
      } catch (error) {
        console.error("Error converting dataURL to Blob:", error);
        return null;
      }
    },

    closeModal() {
      this.showSuccessModal = false;
      if (this.redirectId) {
        this.$router.push(`/qrcode/${this.redirectId}`);
      }
    },

    resetForm() {
      this.formData = new FormData();  // Reset FormData
      // Reset other form fields if needed
    },
    filterNationalities() {
      this.filteredNationalities = this.nationalities.filter((nationality) =>
      nationality.name.toLowerCase().includes(this.formData.nationality.toLowerCase())
      );
    },
    calculateAge() {
      if (!this.formData.date_of_birth) {
        this.formData.age = '';
        return;
      }
      
      const birthDate = new Date(this.formData.date_of_birth);
      const today = new Date();
      let age = today.getFullYear() - birthDate.getFullYear();
      const monthDifference = today.getMonth() - birthDate.getMonth();
      const dayDifference = today.getDate() - birthDate.getDate();
      
      // Adjust age if birthday hasn't happened yet this year
      if (monthDifference < 0 || (monthDifference === 0 && dayDifference < 0)) {
        age--;
      }
      
      this.formData.age = age;
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
    },
    'formData.valid_until'(newDate) {
      if (newDate < this.minDate) {
        this.errorMessage = 'Date must be today or in the future!';
      } else {
        this.errorMessage = '';
      }
    },
    "formData.title"(newTitle) {
      if (newTitle === "Mr.") {
        this.formData.gender = "Male";
      } else if (newTitle === "Ms." || newTitle === "Mrs.") {
        this.formData.gender = "Female";
      } else {
        this.formData.gender = ""; // Reset gender if no title is selected
      }
  },
  }
};
</script>


<style scoped>
.onyx-banner{
  position: relative;
  max-width: 1000px;
  
}
.banner{
  max-width: 1000px;
 position: relative;
  width: 100%;
}

.onyx-header{
  max-width: 800px;
}
.onyx-header h1{
  font-weight: bold;
  color: #003D80;
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
  background-color: #ffffff;
  color: rgb(0, 0, 0);
  border: 1px solid #b0afaf7c;
  border-radius: 3px;
}
.form-group{
  padding: 2rem;
}
.form-consents{
  width: 100%;
  margin-bottom: 1rem;
}

button{
  padding: 0.5rem 1rem;
  border: none;
  background-color: #007bff;
  color: rgb(255, 255, 255);
}

button:hover{
  background-color: #0056b3;
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
.custom-upload span{
  display: inline-block;
    max-width: 150px; /* Adjust based on your layout */
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    vertical-align: middle;
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
  color: rgb(255, 0, 0);
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
/* Modal Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal {
  background: white;
  padding: 20px;
  border-radius: 8px;
  text-align: center;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}

.modal button {
  margin-top: 10px;
  padding: 10px 20px;
  background: #007bff;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 5px;
}

.modal button:hover {
  background: #0056b3;
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
.date{
  height: 35px;
  width: 30vw;
  max-width: 300px;
  background-color: white;
  border: 1px solid grey;
  border-radius: 3px;
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
  background: rgb(218, 4, 25);
  color: white;
}
.label-box{
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.input-info{
  max-width: 900px;
  display: flex;
  flex-direction: column;
}
.input-info input{
  padding: 0.5rem;
  border: 1px solid grey;
  border-radius: 3px;
  height: 35px;
}
.input-info label{
  margin-top: 1rem;
}
.input-info select{
  padding: 0.5rem;
  height: 45px;
  background-color: white;
  color: black;
  border: 1px solid grey;
  border-radius: 3px;
}
.input-info-btn{
  display: flex;
  gap: 2rem;
  margin-top: 1rem;
}
.phone-number{
  height: 45px;
  color: black;
  border: 1px solid grey;
}
.upload{
 background-color: white;
 color: black;
 border: none !important;
}
.dropdown {
  position: relative;
  width: 200px;
  margin-top: 0.7rem;
}

.dropdown input {
  width: 30vw;
  max-width: 300px;
  padding: 0.5rem;
  border: 1px solid grey;
  border-radius: 3px;
}
.upload-container {
  display: flex;
  flex-direction: column;
  gap: 15px;
  width: 300px;
}

.custom-upload {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  background-color: #007bff;
  color: white;
  font-weight: bold;
  padding: 10px 15px;
  border-radius: px;
  cursor: pointer;
  text-align: center;
  transition: background 0.3s ease-in-out;
}

.custom-upload:hover {
  background-color: #0056b3;
}

.custom-upload input {
  display: none;
}

.dropdown-menu {
  position: absolute;
  width: 33vw;
  max-width: 300px;
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
.preview-image{
  max-width: 400px;
  width: 100%;
}
.signature-pad{
  border: 1px solid black;
 
}
h2, h3{
  color: #003D80;
}
.review-section strong{
  color: #003D80;
}
.submit{
  gap: 2rem;
  display: flex;
  margin-top: 1rem;
}
.others{
  margin-top: 0.5rem;
}
@media (max-width: 768px) {
  .upload-container{
    width: 100%;
  }
  .signature-container{
height: 200px;
}

.submit{
  margin-top: 6rem;
  gap: 2rem;
  display: flex;
  z-index: 1;
}
.progress-bar{
  margin-top: 1rem;
}
}
</style>