<template>
  <div class="onyx-form">
    <div class="form-container">
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
            <option value="Mr.">Mr.</option>
            <option value="Mrs.">Mrs.</option>
            <option value="Ms.">Ms.</option>
          </select>
          <input v-model="formData.last_name" placeholder="Enter your last name" required />
          <input v-model="formData.first_name" placeholder="Enter your first name" required />
           <!-- Date of Birth Input -->
    <input 
      type="date" 
      v-model="formData.date_of_birth" 
      @input="calculateAge"
      required 
    />
    
          <input v-model="formData.place_of_birth" placeholder="Place of Birth" required /><br>
          <select v-model="formData.gender">
            <option value="" disabled>Gender</option>
            <option value="Male">Male</option>
            <option value="Female">Female</option>
          </select>
            <!-- Age Input (Auto-Computed) -->
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
    <vue-tel-input
      v-model="formData.mobile_number"
      :preferred-countries="['us', 'gb', 'ph']"
      placeholder="Enter your phone number"
      required
      autocomplete="off"
      ref="phoneInput"
      mode="international"
    />
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
        <div class="verification-info" v-if="currentStep === 4">
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
          <input
  v-model="formData.valid_until"
  type="date"
  placeholder="Valid until"
  required
  :min="minDate"
/>
<p v-if="errorMessage" style="color: red;">{{ errorMessage }}</p>

<label>Upload Front Id:</label>
<input 
  type="file" 
  accept="image/*" 
  capture="environment" 
  @change="handleFileUploadFrontID" 
  required
/>

<label>Upload Back Id:</label>
<input 
  type="file" 
  accept="image/*" 
  capture="environment" 
  @change="handleFileUploadBackID" 
  required
/>

          <input v-model="formData.work_industry" placeholder="Work Industry" required />
          <input v-model="formData.role" placeholder="Role" required />
          <input v-model="formData.income" type="number" placeholder="Income" required />
          <div class="verification-info-btn">
         <button @click="prevStep">Back</button>
         <button @click="nextStep">Next</button>
  </div>
        </div>

        <!-- Step 5: Review & Confirm -->
        <div v-if="currentStep === 5">
          <h2>Step 5: Review & Confirm</h2>
          <h3>Consent and Acknowledgment</h3>

    <!-- Checkbox for Marketing Consent -->
    <label>
      <input type="checkbox" v-model="formData.marketing_consent" />
      I agree to receive promotional offers, advertisements, and marketing communications from CF-ONYX CASINO through email, social media, and/or SMS.
    </label>

    <!-- Checkbox for Data Privacy Agreement -->
    <label>
      <input type="checkbox" v-model="formData.privacy_consent" required />
      I have read and understood this form, including the Privacy Notice, and consent to the processing of my personal data. I acknowledge that I am fully aware of my rights under the Data Privacy Act of 2012 and understand that my consent does not preclude the existence of other lawful grounds for processing my personal data.
    </label>

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
     
    <!-- E-Signature Input -->
    <div class="signature-container">
      <p>E-Signature (Draw below)</p>
      <VueSignaturePad ref="signaturePad" class="signature-pad" />
      <button type="button" @click="clearSignature">Clear</button>
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
      },
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
      }
    },
    toggleList() {
      this.listVisible = !this.listVisible; // Toggle the visibility state
    },
    prevStep() {
      this.currentStep--;
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
      const file = event.target.files[0]; // Get the selected file
      if (file) {
        this.formData.id_front = file;  // Store the file in the id_front property
      }
    },
    handleFileUploadBackID(event) {
      const file = event.target.files[0]; // Get the selected file
      if (file) {
        this.formData.id_back = file;  // Store the file in the id_front property
      }
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
    // Convert the signature to a Base64 image
    const signatureData = this.$refs.signaturePad.saveSignature();
    const base64Image = signatureData.data; // Extract Base64 string

    // Convert Base64 to a Blob (image file)
    const blob = this.dataURLtoBlob(base64Image);
    
    // Create FormData object
    const formData = new FormData();
    formData.append("privacy_consent", this.formData.privacy_consent);
    formData.append("signature", blob, "signature.png");

    // Append other form fields dynamically
    for (const key in this.formData) {
      if (key !== "signature") {
        formData.append(key, this.formData[key]);
      }
    }

    // Make the POST request using axios
    await axios.post("http://192.168.1.11:8000/api/form-records/", formData, {
      headers: {
        "Content-Type": "multipart/form-data", // Ensure Content-Type is set for file uploads
      },
    });

    alert("Form submitted successfully!"); // Show success message
    this.resetForm(); // Reset the form after submission

    // Reload the page after submitting the form
    window.location.reload();
  } catch (error) {
    console.error("Error submitting form:", error); // Log the error
    alert("An error occurred while submitting."); // Show error message
  }
},

dataURLtoBlob(dataURL) {
  // Convert Base64 string to a Blob
  const byteString = atob(dataURL.split(",")[1]);
  const mimeString = dataURL.split(",")[0].split(":")[1].split(";")[0];
  const ab = new ArrayBuffer(byteString.length);
  const ia = new Uint8Array(ab);
  for (let i = 0; i < byteString.length; i++) {
    ia[i] = byteString.charCodeAt(i);
  }
  return new Blob([ab], { type: mimeString });
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
/* Verification Information styling */
.verification-info{
  display: flex;
  flex-direction: column;
  width: 60vw;
  max-width: 900px;
}
.verification-info input{
  padding: 0.5rem;
  margin-top: 1rem;
  max-width: 300px;
}

.verification-info select{
  padding: 0.5rem;
  max-width: 320px;
}
.verification-info-btn {
  display: flex;
  flex-direction: row;
  gap: 1rem;
  margin-top: 1rem;
}
</style>