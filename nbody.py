import math

N = 5
G = 6.67E-11
SUN = 3

t_total = 0.0
dt = 25000.0 # delta t
t = 157788000 # total simulation time
earth = [1.4960e+11, 0.0000e+00, 0.0000e+00, 2.9800e+04, 5.9740e+24]
mars = [2.2790e+11, 0.0000e+00, 0.0000e+00, 2.4100e+04, 6.4190e+23]
mercury = [5.7900e+10, 0.0000e+00, 0.0000e+00, 4.7900e+04, 3.3020e+23]
sun = [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 1.9890e+30]
venus = [1.0820e+11, 0.0000e+00, 0.0000e+00, 3.5000e+04, 4.8690e+24]

# created a nested list containing the input planet data from above
planets = [earth, mars, mercury, sun, venus]

while t_total < t:
    for i in range(N):
        # skip the sun
        if i == 3:
            pass
        else:
            # calculate the radius between i'th planet and the sun
            r = (0.0000e+00 - planets[i][0])**2 + (0.0000e+00 - planets[i][1])**2
            r = math.sqrt(r)
            # calculate the pair-wise force between i'th planet and the sun
            F = G * (1.9890e+30 * planets[i][4]) / r**2
            # calculate the x and y components of the force
            x_force = F * ((0.0000e+00 - planets[i][0]) / r)
            y_force = F * ((0.0000e+00 - planets[i][1]) / r)
            # calculate the x and y components of the acceleration
            x_accel = x_force / planets[i][4]
            y_accel = y_force / planets[i][4]
            # for the current timestep
            # calculate the x and y components of the velocity
            planets[i][2] = planets[i][2] + x_accel * dt
            planets[i][3] = planets[i][3] + y_accel * dt
            # for the next time step
            # calculate the x and y components of the resulting position
            planets[i][0] = planets[i][0] + planets[i][2] * dt
            planets[i][1] = planets[i][1] + planets[i][3] * dt

    # update the time by delta_t
    t_total += dt

# output the formatted values for the x and y components of position/velocity and mass
for i in range(N):
    # print formatted output for each planet
    print([f"{i:.4e}" for i in planets[i]])



