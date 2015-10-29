<?xml version="1.0" ?>
<core:CityModel xmlns:bldg="http://www.opengis.net/citygml/building/1.0" xmlns:core="http://www.opengis.net/citygml/1.0" xmlns:gml="http://www.opengis.net/gml" xmlns:xlink="http://www.w3.org/1999/xlink">
	<gml:name>Project</gml:name>
	<core:cityObjectMember>
		<bldg:Building>
			<gml:name>TestBuilding</gml:name>
			<bldg:function>1120</bldg:function>
			<bldg:yearOfConstruction>1988</bldg:yearOfConstruction>
			<bldg:roofType>1000</bldg:roofType>
			<bldg:measuredHeight uom="m">6.0</bldg:measuredHeight>
			<bldg:storeysAboveGround>2</bldg:storeysAboveGround>
			<bldg:storeyHeightsAboveGround uom="m">3.0 3.0</bldg:storeyHeightsAboveGround>
			<bldg:lod2Solid>
				<gml:Solid>
					<gml:exterior>
						<gml:CompositeSurface>
							<gml:surfaceMember>
								<gml:Polygon gml:id="TestBuilding_ground">
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>-11.057692307692308 -6.5 0.0 11.057692307692308 -6.5 0.0 11.057692307692308 6.5 0.0 -11.057692307692308 6.5 0.0 -11.057692307692308 -6.5 0.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
							<gml:surfaceMember>
								<gml:Polygon gml:id="TestBuilding_roof">
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>-11.057692307692308 -6.5 6.0 11.057692307692308 -6.5 6.0 11.057692307692308 6.5 6.0 -11.057692307692308 6.5 6.0 -11.057692307692308 -6.5 6.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
							<gml:surfaceMember>
								<gml:Polygon gml:id="TestBuilding_a">
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>-11.057692307692308 -6.5 0.0 11.057692307692308 -6.5 0.0 11.057692307692308 -6.5 6.0 -11.057692307692308 -6.5 6.0 -11.057692307692308 -6.5 0.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
							<gml:surfaceMember>
								<gml:Polygon gml:id="TestBuilding_b">
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>-11.057692307692308 6.5 0.0 11.057692307692308 6.5 0.0 11.057692307692308 6.5 6.0 -11.057692307692308 6.5 6.0 -11.057692307692308 6.5 0.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
							<gml:surfaceMember>
								<gml:Polygon gml:id="TestBuilding_c">
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>-11.057692307692308 -6.5 0.0 -11.057692307692308 6.5 0.0 -11.057692307692308 6.5 6.0 -11.057692307692308 -6.5 6.0 -11.057692307692308 -6.5 0.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
							<gml:surfaceMember>
								<gml:Polygon gml:id="TestBuilding_d">
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>11.057692307692308 -6.5 0.0 11.057692307692308 6.5 0.0 11.057692307692308 6.5 6.0 11.057692307692308 -6.5 6.0 11.057692307692308 -6.5 0.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
						</gml:CompositeSurface>
					</gml:exterior>
				</gml:Solid>
			</bldg:lod2Solid>
			<bldg:boundedBy>
				<bldg:FloorSurface gml:id="b_TestBuilding_ground">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember xlink:href="TestBuilding_ground"/>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:FloorSurface>
			</bldg:boundedBy>
			<bldg:boundedBy>
				<bldg:RoofSurface gml:id="b_TestBuilding_roof">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember xlink:href="TestBuilding_roof"/>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:RoofSurface>
			</bldg:boundedBy>
			<bldg:boundedBy>
				<bldg:WallSurface gml:id="b_TestBuilding_a">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember xlink:href="TestBuilding_a"/>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:WallSurface>
			</bldg:boundedBy>
			<bldg:boundedBy>
				<bldg:WallSurface gml:id="b_TestBuilding_b">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember xlink:href="TestBuilding_b"/>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:WallSurface>
			</bldg:boundedBy>
			<bldg:boundedBy>
				<bldg:WallSurface gml:id="b_TestBuilding_c">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember xlink:href="TestBuilding_c"/>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:WallSurface>
			</bldg:boundedBy>
			<bldg:boundedBy>
				<bldg:WallSurface gml:id="b_TestBuilding_d">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember xlink:href="TestBuilding_d"/>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:WallSurface>
			</bldg:boundedBy>
		</bldg:Building>
	</core:cityObjectMember>
	<core:cityObjectMember>
		<bldg:Building>
			<gml:name>TestBuisdfsdfsdflding</gml:name>
			<bldg:function>1120</bldg:function>
			<bldg:yearOfConstruction>1988</bldg:yearOfConstruction>
			<bldg:roofType>1000</bldg:roofType>
			<bldg:measuredHeight uom="m">6.0</bldg:measuredHeight>
			<bldg:storeysAboveGround>2</bldg:storeysAboveGround>
			<bldg:storeyHeightsAboveGround uom="m">3.0 3.0</bldg:storeyHeightsAboveGround>
			<bldg:lod2Solid>
				<gml:Solid>
					<gml:exterior>
						<gml:CompositeSurface>
							<gml:surfaceMember>
								<gml:Polygon gml:id="TestBuisdfsdfsdflding_ground">
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>88.9423076923077 -6.5 0.0 111.0576923076923 -6.5 0.0 111.0576923076923 6.5 0.0 88.9423076923077 6.5 0.0 88.9423076923077 -6.5 0.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
							<gml:surfaceMember>
								<gml:Polygon gml:id="TestBuisdfsdfsdflding_roof">
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>88.9423076923077 -6.5 6.0 111.0576923076923 -6.5 6.0 111.0576923076923 6.5 6.0 88.9423076923077 6.5 6.0 88.9423076923077 -6.5 6.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
							<gml:surfaceMember>
								<gml:Polygon gml:id="TestBuisdfsdfsdflding_a">
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>88.9423076923077 -6.5 0.0 111.0576923076923 -6.5 0.0 111.0576923076923 -6.5 6.0 88.9423076923077 -6.5 6.0 88.9423076923077 -6.5 0.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
							<gml:surfaceMember>
								<gml:Polygon gml:id="TestBuisdfsdfsdflding_b">
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>88.9423076923077 6.5 0.0 111.0576923076923 6.5 0.0 111.0576923076923 6.5 6.0 88.9423076923077 6.5 6.0 88.9423076923077 6.5 0.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
							<gml:surfaceMember>
								<gml:Polygon gml:id="TestBuisdfsdfsdflding_c">
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>88.9423076923077 -6.5 0.0 88.9423076923077 6.5 0.0 88.9423076923077 6.5 6.0 88.9423076923077 -6.5 6.0 88.9423076923077 -6.5 0.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
							<gml:surfaceMember>
								<gml:Polygon gml:id="TestBuisdfsdfsdflding_d">
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>111.0576923076923 -6.5 0.0 111.0576923076923 6.5 0.0 111.0576923076923 6.5 6.0 111.0576923076923 -6.5 6.0 111.0576923076923 -6.5 0.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
						</gml:CompositeSurface>
					</gml:exterior>
				</gml:Solid>
			</bldg:lod2Solid>
			<bldg:boundedBy>
				<bldg:FloorSurface gml:id="b_TestBuisdfsdfsdflding_ground">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember xlink:href="TestBuisdfsdfsdflding_ground"/>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:FloorSurface>
			</bldg:boundedBy>
			<bldg:boundedBy>
				<bldg:RoofSurface gml:id="b_TestBuisdfsdfsdflding_roof">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember xlink:href="TestBuisdfsdfsdflding_roof"/>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:RoofSurface>
			</bldg:boundedBy>
			<bldg:boundedBy>
				<bldg:WallSurface gml:id="b_TestBuisdfsdfsdflding_a">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember xlink:href="TestBuisdfsdfsdflding_a"/>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:WallSurface>
			</bldg:boundedBy>
			<bldg:boundedBy>
				<bldg:WallSurface gml:id="b_TestBuisdfsdfsdflding_b">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember xlink:href="TestBuisdfsdfsdflding_b"/>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:WallSurface>
			</bldg:boundedBy>
			<bldg:boundedBy>
				<bldg:WallSurface gml:id="b_TestBuisdfsdfsdflding_c">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember xlink:href="TestBuisdfsdfsdflding_c"/>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:WallSurface>
			</bldg:boundedBy>
			<bldg:boundedBy>
				<bldg:WallSurface gml:id="b_TestBuisdfsdfsdflding_d">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember xlink:href="TestBuisdfsdfsdflding_d"/>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:WallSurface>
			</bldg:boundedBy>
		</bldg:Building>
	</core:cityObjectMember>
</core:CityModel>
