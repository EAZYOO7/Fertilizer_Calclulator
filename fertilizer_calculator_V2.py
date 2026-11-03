fertilizer = None
nutrient_concentration = None
application_rate = None
nutrient_supplied = None
nutrient_still_required = None

print("\nChoose a nutrient: ")
print("1. Nitrogen")
print("2. Phosphorus")
print("3. Potassium")

Nutrient_choice = input("Enter option number: ")

if Nutrient_choice == "1":
    print("\nChoose from available fertilizers: ")
    print("1. Urea (46)")
    print("2. LAN (28)")
    print("3. 2:3:2 (22)")
    print("4. 3:2:1 (25)")

elif Nutrient_choice == "2":
    print("\nChoose from available fertilizers: ")
    print("1. Superphosphate (50)")
    print("2. 2:3:2 (22)")
    print("3. 3:2:1 (25)")

elif Nutrient_choice == "3":
    print("\nChoose from available fertilizers: ")
    print("1. KCL")
    print("2. 2:3:2 (22)")
    print("3. 3:2:1 (25)")

else:
    print("Invalid selection")
    exit()

choice = input("Enter option number: ")


# ============================================================
# NITROGEN
# ============================================================

if Nutrient_choice == "1":

    if choice == "1":
        fertilizer = "Urea (46)"
        nutrient_concentration = 46

    elif choice == "2":
        fertilizer = "LAN (28)"
        nutrient_concentration = 28

    # --------------------------------------------------------
    # 2:3:2 (22)
    # --------------------------------------------------------

    elif choice == "3":

        fertilizer = "2:3:2 (22)"

        P_required = float(
            input("Enter amount of phosphorous required in kg/ha: ")
        )

        P_nutrient_concentration = 3 / (2 + 3 + 2) * 22

        application_rate = (
            P_required * 100
        ) / P_nutrient_concentration

        print(f"Application rate: {application_rate:.2f} kg/ha")

        # Nitrogen supplied by the compound fertilizer
        nutrient_concentration = 2 / (2 + 3 + 2) * 22

        nutrient_supplied = (
            application_rate * (nutrient_concentration / 100)
        )

        print(f"Nitrogen supplied: {nutrient_supplied:.2f} kg/ha")

        N_required = float(
            input("Enter nitrogen requirements here!: ")
        )

        nutrient_still_required = (
            N_required - nutrient_supplied
        )

        print(
            f"Nitrogen still required: "
            f"{nutrient_still_required:.2f} kg/ha"
        )

    # --------------------------------------------------------
    # 3:2:1 (25)
    # --------------------------------------------------------

    elif choice == "4":

        fertilizer = "3:2:1 (25)"

        P_required = float(
            input("Enter amount of phosphorous required in kg/ha: ")
        )

        P_nutrient_concentration = 2 / (3 + 2 + 1) * 25

        application_rate = (
            P_required * 100
        ) / P_nutrient_concentration

        print(f"Application rate: {application_rate:.2f} kg/ha")

        # Nitrogen supplied
        nutrient_concentration = 3 / (3 + 2 + 1) * 25

        nutrient_supplied = (
            application_rate * (nutrient_concentration / 100)
        )

        print(f"Nitrogen supplied: {nutrient_supplied:.2f} kg/ha")

        N_required = float(
            input("Enter nitrogen requirements here!: ")
        )

        nutrient_still_required = (
            N_required - nutrient_supplied
        )

        print(
            f"Nitrogen still required: "
            f"{nutrient_still_required:.2f} kg/ha"
        )

    else:
        print("Invalid selection")
        exit()


# ============================================================
# PHOSPHORUS
# ============================================================

elif Nutrient_choice == "2":

    if choice == "1":

        fertilizer = "Superphosphate (50)"
        nutrient_concentration = 50

    elif choice == "2":

        fertilizer = "2:3:2 (22)"

        P_required = float(
            input("Enter amount of phosphorous required in kg/ha: ")
        )

        P_nutrient_concentration = 3 / (2 + 3 + 2) * 22

        application_rate = (
            P_required * 100
        ) / P_nutrient_concentration

        print(f"Application rate: {application_rate:.2f} kg/ha")

        # Store concentration for summary
        nutrient_concentration = P_nutrient_concentration

    elif choice == "3":

        fertilizer = "3:2:1 (25)"

        P_required = float(
            input("Enter amount of phosphorous required in kg/ha: ")
        )

        P_nutrient_concentration = 2 / (3 + 2 + 1) * 25

        application_rate = (
            P_required * 100
        ) / P_nutrient_concentration

        print(f"Application rate: {application_rate:.2f} kg/ha")

        # Store concentration for summary
        nutrient_concentration = P_nutrient_concentration

    else:
        print("Invalid selection")
        exit()


# ============================================================
# POTASSIUM
# ============================================================

elif Nutrient_choice == "3":

    if choice == "1":

        fertilizer = "KCL"
        nutrient_concentration = 10.5

    elif choice == "2":

        fertilizer = "2:3:2 (22)"

        P_required = float(
            input("Enter amount of phosphorous required in kg/ha: ")
        )

        P_nutrient_concentration = 3 / (2 + 3 + 2) * 22

        application_rate = (
            P_required * 100
        ) / P_nutrient_concentration

        print(f"Application rate: {application_rate:.2f} kg/ha")

        # Potassium supplied
        nutrient_concentration = 2 / (2 + 3 + 2) * 22

        K_supplied = (
            application_rate * (nutrient_concentration / 100)
        )

        print(f"Potassium supplied: {K_supplied:.2f} kg/ha")

        K_required = float(
            input("Enter Potassium requirements here!: ")
        )

        K_still_required = (
            K_required - K_supplied
        )

        print(
            f"Potassium still required: "
            f"{K_still_required:.2f} kg/ha"
        )

    elif choice == "3":

        fertilizer = "3:2:1 (25)"

        P_required = float(
            input("Enter amount of phosphorous required in kg/ha: ")
        )

        P_nutrient_concentration = 2 / (3 + 2 + 1) * 25

        application_rate = (
            P_required * 100
        ) / P_nutrient_concentration

        print(f"Application rate: {application_rate:.2f} kg/ha")

        # Potassium supplied
        nutrient_concentration = 1 / (3 + 2 + 1) * 25

        K_supplied = (
            application_rate * (nutrient_concentration / 100)
        )

        print(f"Potassium supplied: {K_supplied:.2f} kg/ha")

        K_required = float(
            input("Enter Potassium requirements here!: ")
        )

        K_still_required = (
            K_required - K_supplied
        )

        print(
            f"Potassium still required: "
            f"{K_still_required:.2f} kg/ha"
        )

    else:
        print("Invalid selection")
        exit()


# ============================================================
# SIMPLE FERTILIZER CALCULATION
# ============================================================

if application_rate is None:

    print(f"\nFertilizer selected: {fertilizer}")

    N_required = float(
        input("Enter nutrient requirements in here!: ")
    )

    application_rate = (
        N_required * 100
    ) / nutrient_concentration

    print(
        f"Application rate: "
        f"{application_rate:.2f} kg/ha"
    )


# ============================================================
# CALCULATION SUMMARY
# ============================================================

print("\n" + "=" * 50)
print("              CALCULATION SUMMARY")
print("=" * 50)

print(f"Fertilizer: {fertilizer}")
print(f"Application rate: {application_rate:.2f} kg/ha")

# ------------------------------------------------------------
# SIMPLE FERTILIZER SUMMARY
# ------------------------------------------------------------

if nutrient_supplied is None:

    print(f"Nutrient concentration: "
          f"{nutrient_concentration:.2f}%")

    print("\nFormula:")
    print("Application Rate = "
          "(Nutrient Required × 100) "
          "÷ Nutrient Concentration")

    print("\nCalculation:")
    print(
        f"Application Rate = "
        f"({N_required:.2f} × 100) "
        f"÷ {nutrient_concentration:.2f}"
    )

    print(
        f"\nResult: "
        f"{application_rate:.2f} kg/ha"
    )


# ------------------------------------------------------------
# COMPLETE FERTILIZER SUMMARY
# ------------------------------------------------------------

else:

    print("\n--- COMPLETE FERTILIZER CALCULATION ---")

    print("\nSTEP 1: Determine nutrient concentration")

    print("Formula:")
    print(
        "Nutrient Concentration = "
        "(Nutrient ratio ÷ Total ratio) "
        "× Fertilizer analysis"
    )

    print("\nSTEP 2: Determine application rate")

    print("Formula:")
    print(
        "Application Rate = "
        "(P Required × 100) "
        "÷ P Concentration"
    )

    print(
        f"\nP Required: {P_required:.2f} kg/ha"
    )

    print(
        f"P Concentration: "
        f"{P_nutrient_concentration:.4f}%"
    )

    print(
        f"Application Rate: "
        f"{application_rate:.2f} kg/ha"
    )

    print("\nSTEP 3: Determine nutrient supplied")

    print("Formula:")
    print(
        "Nutrient Supplied = "
        "Application Rate × "
        "(Nutrient Concentration ÷ 100)"
    )

    print(
        f"\nNutrient Supplied: "
        f"{nutrient_supplied:.2f} kg/ha"
    )

    print("\nSTEP 4: Determine nutrient still required")

    print("Formula:")
    print(
        "Nutrient Still Required = "
        "Nutrient Required − Nutrient Supplied"
    )

    print(
        f"\nNutrient Still Required: "
        f"{nutrient_still_required:.2f} kg/ha"
    )

print("=" * 50)