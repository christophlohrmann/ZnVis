"""
ZnVis: A Zincwarecode package.
License
-------
This program and the accompanying materials are made available under the terms
of the Eclipse Public License v2.0 which accompanies this distribution, and is
available at https://www.eclipse.org/legal/epl-v20.html
SPDX-License-Identifier: EPL-2.0
Copyright Contributors to the Zincwarecode Project.
Contact Information
-------------------
email: zincwarecode@gmail.com
github: https://github.com/zincware
web: https://zincwarecode.com/
Citation
--------
If you use this module please cite us with:

Summary
-------
Tutorial script to visualize simple spheres over a random trajectory.
"""
import numpy as np

import znvis as vis

if __name__ == "__main__":
    """
    Run the simple spheres example.
    """
    # Define the first particle.
    trajectory = np.random.uniform(-10, 10, (10, 10, 3))
    mesh = vis.Sphere(radius=2.0, colour=np.array([30, 144, 255]) / 255, resolution=10)
    particle = vis.Particle(name="Blue", mesh=mesh, position=trajectory)

    # Define the second particle.
    trajectory_2 = np.random.uniform(-10, 10, (10, 10, 3))
    mesh_2 = vis.Sphere(radius=1.0, colour=np.array([255, 140, 0]) / 255, resolution=10)
    particle_2 = vis.Particle(name="Orange", mesh=mesh_2, position=trajectory_2)

    # Construct the visualizer and run
    visualizer = vis.Visualizer(particles=[particle, particle_2], frame_rate=20)
    visualizer.run_visualization()
