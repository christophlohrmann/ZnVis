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
Example script for visualizing simple cylinders.
"""
import numpy as np

import znvis as vis

if __name__ == "__main__":
    """
    Run the simple spheres example.
    """
    # Define the first particle.
    trajectory = np.random.uniform(-5, 5, size=(10, 10, 3))
    orientation = np.random.uniform(0, 1, size=(10, 10, 3))
    mesh = vis.Cylinder(
        radius=0.2, height=3.0, colour=np.array([30, 144, 255]) / 255, resolution=10
    )
    particle = vis.Particle(
        name="Blue", mesh=mesh, position=trajectory, director=orientation
    )

    # Construct the visualizer and run
    visualizer = vis.Visualizer(particles=[particle], frame_rate=10)
    visualizer.run_visualization()
